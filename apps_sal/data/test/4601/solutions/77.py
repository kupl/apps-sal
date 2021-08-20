(N, K) = map(int, input().split())
H = list(map(int, input().split()))
H = sorted(H, reverse=True)
ans = 0
if N > K:
    ans = sum(H[K:])
print(ans)
