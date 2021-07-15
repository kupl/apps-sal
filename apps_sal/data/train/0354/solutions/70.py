class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def init():
            return [[0 for _ in range(20)] for _ in range(7)]
        st = init()
        pst = init()
        for i in range(1, 7):
            pst[i][1] = 1
            
        for _ in range(1, n):
            for i in range(1, 7):
                st[i][1] = 0
                for j in range(1, 7):
                    if i != j:
                        st[i][1] += sum(pst[j])
                for j in range(2, rollMax[i - 1] + 1):
                    st[i][j] = pst[i][j - 1]
            st, pst = pst, st
        return sum([sum(r) for r in pst]) % 1000000007
