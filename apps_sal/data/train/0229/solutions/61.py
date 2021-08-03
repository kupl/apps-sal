class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort(key=lambda x: abs(x))
        c = {}
        for v in A:
            if v / 2 in c:
                c[v / 2] -= 1
                if not c[v / 2]:
                    del c[v / 2]
            else:
                if v not in c:
                    c[v] = 0
                c[v] += 1
        return len(c) == 0
