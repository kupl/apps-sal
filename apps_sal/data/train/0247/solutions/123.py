class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        nums = [0 for i in range(len(arr))]
        nums[0] = arr[0]
        for i in range(1, len(arr)):
            nums[i] = nums[i - 1] + arr[i]
        best = [float('inf') for i in range(len(arr))]
        ans = float('inf')
        size = float('inf')
        l = 0
        r = 0
        window = 0
        while l <= r and r < len(arr):
            window += arr[r]
            while l <= r and window > target:
                window -= arr[l]
                l += 1
            if window == target:
                ans = min(ans, r - l + 1 + best[l - 1])
                best[r] = min(best[r - 1], r - l + 1)
            else:
                best[r] = best[r - 1]
            r += 1
        if ans == float('inf'):
            return -1
        else:
            return ans
