class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        alls = []
        n = len(arr)
        alls.append([1, n])

        count = n

        if m == n:
            return n

        for j in range(len(arr)):
            a = arr[n - j - 1]

            count -= 1
            for i in range(len(alls)):
                if a >= alls[i][0] and a <= alls[i][1]:
                    left = [alls[i][0], a - 1]
                    right = [a + 1, alls[i][1]]

                    del alls[i]

                    if left[1] - left[0] == m - 1:
                        return count

                    if right[1] - right[0] == m - 1:
                        return count

                    if left[1] >= left[0] and left[1] - left[0] > m - 1:
                        alls.append(left)
                    if right[1] >= right[0] and right[1] - right[0] > m - 1:
                        alls.append(right)

                    break
            # print(alls)

        return -1
