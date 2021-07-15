class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)
        s = set()
        diff = 0
        for i in range(26):
            c = chr(ord('a') + i)
            diff += c1[c] - c2[c]
            if diff:
                s.add(diff > 0)
        return len(s) < 2
