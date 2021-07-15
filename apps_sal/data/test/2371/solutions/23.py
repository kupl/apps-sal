N, Z, W = map(int, input().split())
a = list(map(int, input().split()))

ans = abs(W - a[-1])
if N > 1:
    ans = max(ans, abs(a[-2] - a[-1]))
print(ans)
