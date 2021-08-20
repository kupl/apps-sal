class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        m = dict(a=1, e=2, i=4, o=8, u=16)
        longest = 0
        parity_index = {0: -1}
        parity = 0
        for (i, ch) in enumerate(s):
            if ch in m:
                parity = parity ^ m[ch]
            if parity not in parity_index:
                parity_index[parity] = i
            else:
                longest = max(longest, i - parity_index.get(parity))
        return longest
