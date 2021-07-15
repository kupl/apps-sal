class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        
        dd = Counter(A)
        A.sort(key = lambda a : abs(a))

        for a in A:
            if a in dd and dd[a]:
                if 2*a in dd and dd[2*a]:
                    dd[a] -= 1
                    dd[2*a] -= 1
                    if dd[a] == 0:
                        del dd[a]
                    if dd[a*2] == 0:
                        del dd[a*2]
                else:
                    return False
        return True
