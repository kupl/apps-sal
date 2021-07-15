N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = N * M - sum(A)

if ans < 0:
    print(0)
elif ans > K:
    print(-1)
else:
    print(ans)
