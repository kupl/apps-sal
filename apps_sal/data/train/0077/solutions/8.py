import sys
input = sys.stdin.readline

Q = int(input())
data = []
for _ in range(Q):
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    data.append([N, A, B])

for N, A, B in data:
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0][1] = B[0]
    dp[0][2] = 2*B[0]
    for i in range(1, N):
        if A[i] == A[i-1]:
            dp[i][0] = min(dp[i-1][1], dp[i-1][2])
        elif A[i] == A[i-1]+1:
            dp[i][0] = min(dp[i-1][0], dp[i-1][2])
        elif A[i] == A[i-1]+2:
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])
        else:
            dp[i][0] = min([dp[i-1][0], dp[i-1][1], dp[i-1][2]])
        
        if A[i] == A[i-1]+1:
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + B[i]
        elif A[i] == A[i-1]:
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + B[i]
        elif A[i] == A[i-1]-1:
            dp[i][1] = min(dp[i-1][1], dp[i-1][2]) + B[i]
        else:
            dp[i][1] = min([dp[i-1][0], dp[i-1][1], dp[i-1][2]]) + B[i]
        
        if A[i] == A[i-1]:
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + 2*B[i]
        elif A[i] == A[i-1]-1:
            dp[i][2] = min(dp[i-1][0], dp[i-1][2]) + 2*B[i]
        elif A[i] == A[i-1]-2:
            dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + 2*B[i]
        else:
            dp[i][2] = min([dp[i-1][0], dp[i-1][1], dp[i-1][2]]) + 2*B[i]
    ans = min(dp[N-1])
    print(ans)


