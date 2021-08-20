class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = len(arr) + 1
        best_idx = [INF] * len(arr)
        best = INF
        csum = 0
        left = 0
        for right in range(len(arr)):
            csum += arr[right]
            while csum > target and left <= right:
                csum -= arr[left]
                left += 1
            if csum == target:
                best = min(best, best_idx[left - 1] + right - left + 1)
                best_idx[right] = min(best_idx[right - 1], right - left + 1)
            else:
                best_idx[right] = best_idx[right - 1]
        if INF == best:
            return -1
        return best


"\nclass Solution:\n    def minSumOfLengths(self, arr: List[int], target: int) -> int:\n        INF = len(arr) + 1\n        best_at_i = [INF]*len(arr) # the ith index represents the smallest length subarray we've found ending <= i that sums to target\n        best = INF # output \n        curr_sum = 0 # current sum between left and right\n        \n        left = 0\n        for right in range(len(arr)):\n            # update the running sum\n            curr_sum += arr[right]\n            \n            # arr is strictly positive, so shrink window until we're not above target\n            while curr_sum > target and left <= right:\n                curr_sum -= arr[left]\n                left += 1\n                \n            if curr_sum == target:\n                # we have a new shortest candidate to consider\n                best = min(best, best_at_i[left-1] + right - left + 1)\n                best_at_i[right] = min(best_at_i[right-1], right - left + 1)\n            else:\n                # best we've seen is the previous best (overlaps to end if right == 0)\n                best_at_i[right] = best_at_i[right-1]\n\n        if best == INF:\n            return -1\n        return best"
