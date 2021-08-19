class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        ans1 = True
        ans2 = True
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                ans1 = False
            if s2[i] < s1[i]:
                ans2 = False
        return ans1 or ans2
