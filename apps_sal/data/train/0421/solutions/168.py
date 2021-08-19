class Solution:

    def lastSubstring(self, s: str) -> str:
        d = defaultdict(list)
        for (i, c) in enumerate(s):
            d[c].append(i)
        z = max(d.keys())
        ids = d[z]
        return max((s[start:] for start in ids))
