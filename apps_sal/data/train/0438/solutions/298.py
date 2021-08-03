class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        A = [0 for _ in range(n + 2)]
        left = [-1 for _ in range(n + 2)]
        right = [-1 for _ in range(n + 2)]
        count = 0
        res = -1

        for i, a in enumerate(arr):
            if A[a - 1] == 0 and A[a + 1] == 0:
                left[a] = a
                right[a] = a
            elif A[a - 1] == 0:
                if abs(left[a + 1] - right[a + 1]) + 1 == m:
                    count -= 1
                left[a] = a
                right[a] = right[a + 1]
                left[right[a]] = a
            elif A[a + 1] == 0:
                if abs(left[a - 1] - right[a - 1]) + 1 == m:
                    count -= 1
                left[a] = left[a - 1]
                right[a] = a
                right[left[a]] = a
            else:
                if abs(left[a + 1] - right[a + 1]) + 1 == m:
                    count -= 1
                if abs(left[a - 1] - right[a - 1]) + 1 == m:
                    count -= 1
                left[a] = left[a - 1]
                right[a] = right[a + 1]
                right[left[a]] = right[a]
                left[right[a]] = left[a]

            A[a] = 1
            if abs(left[a] - right[a]) + 1 == m:
                count += 1
            if count >= 1:
                res = i + 1

            # print(left, right, res, count)

        return res
