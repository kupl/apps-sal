N,A = (int(T) for T in input().split())
X = [int(T) for T in input().split()]
DP = [[[0]*(N+1) for TS in range(0,50*N+1)] for TI in range(0,N+1)]
DP[0][0][0] = 1
for TI in range(0,N):
    for TS in range(0,50*N+1):
        for TK in range(0,N+1):
            if DP[TI][TS][TK]!=0:
                DP[TI+1][TS][TK] += DP[TI][TS][TK]
                DP[TI+1][TS+X[TI]][TK+1] += DP[TI][TS][TK]
print(sum(DP[N][A*TA][TA] for TA in range(1,N+1)))
