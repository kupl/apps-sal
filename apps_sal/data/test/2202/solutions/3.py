N, P = list(map(int, input().split()))
src = list(map(int, input().split()))
K = sum(src) % P
ans = tmp = 0
for a in src:
    tmp += a
    tmp %= P
    ans = max(ans, tmp + (K - tmp) % P)
print(ans)
