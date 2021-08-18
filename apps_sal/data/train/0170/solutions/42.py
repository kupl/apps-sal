class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        left = [False] * n
        right = [False] * n

        left[0] = True
        right[n - 1] = True
        for i in range(1, n):
            left[i] = left[i - 1] and (arr[i] >= arr[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] and (arr[i] <= arr[i + 1])

        def isPossible(num):
            res = False
            for i in range(n):
                if i == 0 or left[i - 1]:
                    if i + num >= n or (right[i + num] and (i == 0 or arr[i - 1] <= arr[i + num])):
                        res = True
                        break
            return res

        be = 0
        en = n - 1

        while be < en:
            mid = be + (en - be) // 2
            if isPossible(mid):
                en = mid
            else:
                be = mid + 1

        return be
