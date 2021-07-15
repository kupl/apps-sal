class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        d = {}
        
        for n in arr:
            d[n] = d.get(n - difference, 0) + 1     
        return max(d.values())
