class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        m = dict(a=1, e=0b10, i=0b100, o=0b1000, u=0b10000)
        longest = 0
        parity_index = {0: -1}
        parity = 0
        for i, ch in enumerate(s):
            if ch in m:
                parity = parity ^ m[ch]
            if parity not in parity_index:
                parity_index[parity] = i
            else:
                longest = max(longest, i - parity_index.get(parity))
        return longest                
