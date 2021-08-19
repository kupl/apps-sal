class Solution:

    def checkIfCanBreak(self, s1, s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        return all((x <= y for (x, y) in zip(s1, s2))) or all((y <= x for (x, y) in zip(s1, s2)))
