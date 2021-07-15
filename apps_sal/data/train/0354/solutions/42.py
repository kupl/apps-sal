class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        p = 10**9 + 7
        C = [[[0 for v in range(rollMax[i])] for i in range(6)] for k in range(n)]
        for i in range(6):
            C[0][i][0] = 1
        for k in range(n-1):
            A = {}
            for i in range(6):
                for v in range(rollMax[i]-1):
                    A[(i,v+1)] = C[k][i][v]
                A[(i,0)] = sum([C[k][i1][v] for i1 in range(6) for v in range(rollMax[i1]) if i1!=i])
            for i in range(6):
                for v in range(rollMax[i]):
                    C[k+1][i][v] = A[(i,v)]%p
#        print(C)
        return(sum([sum(row) for row in C[-1]])%p)
