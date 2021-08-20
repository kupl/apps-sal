class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted([c for c in s1])
        s2 = sorted([c for c in s2])
        return all((char1 <= char2 for (char1, char2) in zip(s1, s2))) or all((char1 >= char2 for (char1, char2) in zip(s1, s2)))
