class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        memo = [[1, len(arr)]]
        if m == len(arr):
            return len(arr)
        for j in range(len(arr) - 1, -1, -1):
            i = arr[j]
            (left, right) = (0, len(memo) - 1)
            while left <= right:
                mid = (left + right) // 2
                if memo[mid][0] <= i:
                    left = mid + 1
                else:
                    right = mid - 1
            (a, b) = (memo[right][0], memo[right][1])
            if i - a == m or a + b - i - 1 == m:
                return j
            flag = True
            if i - a > 0:
                memo[right][1] = i - a
            else:
                memo.pop(right)
                flag = False
            if a + b - i - 1 > 0:
                memo[right + flag:right + flag] = [[i + 1, a + b - i - 1]]
        return -1
