from collections import defaultdict


class Solution:

    def findTheLongestSubstring(self, string: str) -> int:
        vowels = 'aeiou'
        vowels_dict = dict(zip(vowels, range(5)))
        curr = 0
        pos_dict = defaultdict(lambda: float('inf'))
        pos_dict[0] = -1
        res = 0
        for (i, v) in enumerate(string):
            if v in vowels_dict:
                curr ^= 1 << vowels_dict[v]
            res = max(res, i - pos_dict[curr])
            pos_dict[curr] = min(pos_dict[curr], i)
        return res
