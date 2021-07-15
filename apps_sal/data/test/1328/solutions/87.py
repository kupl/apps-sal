N,Ma,Mb = map(int,input().split())
Data = []
for _ in range(N):
    a,b,c = map(int,input().split())
    Data.append([a,b,c])

DP = []
for _ in range(N+1):
    temp = [[-1]*(N*10+1) for _ in range(N*10+1)]
    DP.append(temp)
DP[0][0][0] = 0

for i in range(1,N+1):
    A,B,C = Data[i-1]
    for a in range(0,N*10+1):
        for b in range(0,N*10+1):
            if DP[i-1][a][b] != -1:
                # 使わない
                if DP[i][a][b] == -1:
                    DP[i][a][b] = DP[i-1][a][b]
                else:
                    DP[i][a][b] = min(DP[i][a][b],DP[i-1][a][b])

                #使う
                if DP[i][a+A][b+B] == -1:
                    DP[i][a+A][b+B] = DP[i-1][a][b]+C
                else:
                    DP[i][a+A][b+B] = min(DP[i][a+A][b+B],DP[i-1][a][b]+C)
ans = -1
for a in range(1,N*10+1):
    for b in range(1,N*10+1):
        if DP[N][a][b] != -1 and a * Mb == b * Ma:
            if ans == -1:
                ans = DP[N][a][b]
            else:
                ans = min(ans,DP[N][a][b])
print(ans)
