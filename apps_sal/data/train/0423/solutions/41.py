from collections import defaultdict


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        elemToLen = defaultdict(int)
        best = 0
        for x in arr:
            elemToLen[x] = max(elemToLen[x], elemToLen[x - difference] + 1)
            best = max(best, elemToLen[x])
        return best
