class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        at0 = 0
        at1 = 0

        num0 = 0
        for a in S:
            if a == '0':
                at1 = min(at1, at0) + 1
            else:
                at1 = min(at1, at0)
                at0 += 1

            # print(at0,at1)
        return min(at1, at0)
