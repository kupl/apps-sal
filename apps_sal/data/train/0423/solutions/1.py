class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hs = dict()
        for num in arr:
            if num - difference in hs:
                hs[num] = hs[num - difference] + 1
            if num not in hs and num - difference not in hs:
                hs[num] = 1
        return max((item for item in hs.values()))
