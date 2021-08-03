class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        odds = 0
        for v in d.values():
            if v % 2 == 1:
                odds += 1
        return odds <= k and k <= len(s)
