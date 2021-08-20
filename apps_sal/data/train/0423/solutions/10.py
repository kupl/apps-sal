class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = dict()
        max_seq = 0
        for a in arr:
            res[a] = res.get(a - difference, 0) + 1
        return max(res.values())
