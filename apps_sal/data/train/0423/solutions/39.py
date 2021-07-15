class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        memo=dict()
        #arr.sort()
        for a in arr:
            if a-d in list(memo.keys()):
                memo[a]=memo[a-d]+1
            else:
                memo[a]=1
        return max(list(memo.values()))

