class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seq = {}
        for a in arr:
            seq[a] = max(seq.get(a, 0), seq.pop(a - difference, 0) + 1)
        return max(seq.values())
