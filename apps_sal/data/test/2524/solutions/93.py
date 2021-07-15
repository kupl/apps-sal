N, *A = map(int, open(0).read().split())
mod = 10**9 + 7

ans = 0
for i in range(60):
    mask = 1 << i
    cnt = 0
    for a in A:
        if a & mask:
            cnt += 1
    x = cnt * (N-cnt)
    x *= mask % mod
    ans += x
    ans %= mod

print(ans)
