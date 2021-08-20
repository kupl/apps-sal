class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mp = {}
        res = 0
        for num in arr:
            currlen = 1
            if num - difference in mp:
                currlen = mp[num - difference] + 1
            mp[num] = max(mp.get(num, 1), currlen)
            res = max(res, currlen)
        return res
