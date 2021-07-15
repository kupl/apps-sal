class Solution:
    def lastSubstring(self, s: str) -> str:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        z = max(d.keys())                   # max char
        ids = d[z]                                # start pos for substrings
        return max(s[start:] for start in ids)
