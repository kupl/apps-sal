class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans, d = 0, defaultdict(lambda: (-1, -1))
        for i, c in enumerate(s):
            ans += (d[c][1]-d[c][0])*(i-d[c][1])
            d[c] = (d[c][1], i)
        for c, pre in d.items():
            ans += (d[c][1]-d[c][0])*(len(s)-d[c][1])
        return ans
