class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix, suffix = [float('inf')] * len(arr), [float('inf')] * len(arr)
        curSum, l = 0, 0
        for r in range(1, len(arr)):
            prefix[r] = prefix[r - 1]
            curSum += arr[r - 1]
            while curSum >= target:
                if curSum == target:
                    prefix[r] = min(prefix[r], r - l)
                curSum -= arr[l]
                l += 1
        curSum, r = 0, len(arr)
        for l in range(len(arr) - 1, 0, -1):
            if l < len(arr) - 1:
                suffix[l] = suffix[l + 1]
            curSum += arr[l]
            while curSum >= target:
                if curSum == target:
                    suffix[l] = min(suffix[l], r - l)
                curSum -= arr[r - 1]
                r -= 1

        res = len(arr) + 1
        for i in range(1, len(arr) - 1):
            res = min(res, prefix[i] + suffix[i])
        return res if res <= len(arr) else -1
