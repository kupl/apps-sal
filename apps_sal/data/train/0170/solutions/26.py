class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = res = 0
        r = n = len(arr)
        increasing = [0] * n

        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                increasing[i] = 1 + increasing[i - 1]
        # print(arr)
        # print(increasing)
        while l < r:
            mid = (l + r) // 2
            # print(mid)
            for i in range(n - mid + 1):
                isLeftInc = False
                isRightInc = False
                if i > 0 and increasing[i - 1] == i - 1 or i == 0:
                    isLeftInc = True

                if (i < n - mid and increasing[n - 1] >= n - i - mid - 1 and arr[i + mid] >= (0 if i < 1 else arr[i - 1])) or i == n - mid:
                    isRightInc = True
                # print(i, isLeftInc, isRightInc, i + mid, i-1)

                if isLeftInc and isRightInc:
                    break

            if isLeftInc and isRightInc:
                res = mid
                r = mid
            else:
                l = mid + 1

        return res
