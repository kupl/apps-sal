N, Z, W = map(int, input().split())
A = list(map(int, input().split()))

ans = abs(A[-1] - W)

if N >= 2:
    ans = max(ans, abs(A[-2] - A[-1]))

print(ans)
