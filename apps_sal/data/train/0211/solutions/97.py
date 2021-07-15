import itertools
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        maxres = 1
        for sep in itertools.product([0,1], repeat = len(s)-1):
            # print(sep)
            sett = set()
            cur = s[0]
            for i,(se,c) in enumerate(zip(sep, s[1:]), start=1):
                if se:
                    if cur in sett:
                        break
                    sett.add(cur)
                    cur = c
                else:
                    cur += c
            else:
                if cur in sett:
                    continue
                sett.add(cur)
                # print(sep, sett)
                maxres = max(maxres, len(sett))
        return maxres
        

