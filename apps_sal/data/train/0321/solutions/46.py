class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = sorted(list(s1))
        l2 = sorted(list(s2))
        case1 = True
        case2 = True
        for i in range(len(l1)):
            if l1[i] > l2[i]:
                case1 = False
        for i in range(len(l1)):
            if l2[i] > l1[i]:
                case2 = False
        return case1 or case2
