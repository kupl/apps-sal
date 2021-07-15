class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1list = list(s1)
        s2list = list(s2)
        s1list.sort()
        s2list.sort()
        count1 = 0
        count2 = 0
        for i in range(len(s1)):
            count1 += int(s1list[i] >= s2list[i])
        for i in range(len(s1)):
            count2 += int(s2list[i] >= s1list[i])
        return (not count1%len(s1) or not count2%len(s1))

