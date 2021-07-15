class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        if not arr:
            return 0
        cache={}
        maxc=0
        for i in arr:
            if i-d in cache:
                cache[i]=cache[i-d]+1
            else:
                cache[i]=1
            maxc=max(maxc,cache[i])
        return maxc
