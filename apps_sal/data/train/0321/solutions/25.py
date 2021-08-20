class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return all((ch1 <= ch2 for (ch1, ch2) in zip(sorted(s1), sorted(s2)))) or all((ch1 <= ch2 for (ch1, ch2) in zip(sorted(s2), sorted(s1))))
