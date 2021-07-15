class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        max_val = 10000
        min_val = -10000
        diff = [0 for i in range(max_val - min_val + 1)]
        res = 1
        for x in arr:
            if x - difference >= min_val and x - difference <= max_val and diff[x-difference+max_val] >= diff[x+max_val]:
                diff[x+max_val] = diff[x-difference+max_val] + 1
            else:
                diff[x+max_val] = max(1, diff[x+max_val])
            res = max(res, diff[x+max_val])
        return res

