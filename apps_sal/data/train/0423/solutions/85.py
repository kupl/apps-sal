class Solution:

    def longestSubsequence(self, arr: List[int], d: int) -> int:
        mp = {}
        for (i, a) in enumerate(arr):
            if a - d in mp:
                mp[a] = mp[a - d] + 1
            else:
                mp[a] = 1
        return max(mp.values())
