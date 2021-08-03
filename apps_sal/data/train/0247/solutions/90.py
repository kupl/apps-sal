class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        minlen = [float('inf')] * len(arr)
        res = float('inf')
        l, r, windsum = 0, 0, 0
        for r in range(len(arr)):
            windsum += arr[r]
            while windsum > target:
                windsum -= arr[l]
                l += 1
            if windsum == target:
                if minlen[l - 1] != float('inf'):
                    temp = minlen[l - 1] + r - l + 1
                    res = min(res, temp)
                minlen[r] = min(minlen[r - 1], r - l + 1)
            else:
                minlen[r] = minlen[r - 1]
        return res if res < float('inf') else -1
