class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        t1, t2 = sorted(list(s1)), sorted(list(s2))
        for i in range(len(t1)):
            if t1[i] <= t2[i]:
                continue
            else:
                break
        else:
            return True

        for i in range(len(t1)):
            if t1[i] >= t2[i]:
                continue
            else:
                break
        else:
            return True

        return False
