class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = [char for char in s1]
        l1.sort()
        l2 = [char for char in s2]
        l2.sort()
        strlen = len(s1)
        flag = 0
        for i in range(strlen):
            if l1[i] >= l2[i]:
                continue
            else:
                flag = 1
                break
        if flag:
            for i in range(strlen):
                if l1[i] <= l2[i]:
                    continue
                else:
                    return False
        return True
