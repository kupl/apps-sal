N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
A = sorted(AB,key=lambda x:x[0])
ans = 0

for i in range(N):
    buy = min(M,A[i][1])
    ans += buy * A[i][0]
    M -= buy
print(ans)
