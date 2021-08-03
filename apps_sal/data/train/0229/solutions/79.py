import numpy as np


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        statdict = {}
        flag = True
#        print(A)
        for i in A:
            #            print(statdict)
            if i in statdict:
                statdict[i] = statdict[i] + 1
            elif i < 0:
                if i * 2 in statdict:
                    statdict[i * 2] = statdict[i * 2] - 1
                    if statdict[i * 2] == 0:
                        statdict.pop(i * 2)
                else:
                    statdict[i] = 1
            else:
                if (i % 2 == 0) and i / 2 in statdict:
                    statdict[int(i / 2)] = statdict[int(i / 2)] - 1
                    if statdict[int(i / 2)] == 0:
                        statdict.pop(int(i / 2))
                else:
                    statdict[i] = 1
        return (len(statdict) == 0) or (len(statdict) == 1 and 0 in statdict and statdict[0] % 2 == 0)
