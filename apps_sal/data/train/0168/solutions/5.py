class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        c = Counter(s)
        return sum(c.values()) >= k and len([v for v in c.values() if v % 2]) <= k
