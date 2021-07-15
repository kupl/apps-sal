class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return all([a <= b for a, b in zip(sorted(s1), sorted(s2))]) or all([b <= a for a, b in zip(sorted(s1), sorted(s2))])
