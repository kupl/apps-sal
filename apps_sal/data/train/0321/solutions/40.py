class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ans1 = [a <= b for (a, b) in zip(sorted(s1), sorted(s2))]
        ans2 = [a >= b for (a, b) in zip(sorted(s1), sorted(s2))]
        if len(set(ans1)) == 1 or len(set(ans2)) == 1:
            return True
        return False
