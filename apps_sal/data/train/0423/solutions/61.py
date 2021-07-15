class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d , ans = defaultdict(int) , 0
        for i in arr:
            d[i] = d[i-difference] + 1
            ans = max(ans,d[i])
        return(ans)
