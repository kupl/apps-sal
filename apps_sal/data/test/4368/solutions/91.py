N, K = map(int,input().split())
ans = 1
while(N >= K):
    N = N//K
    ans += 1
print(ans)
