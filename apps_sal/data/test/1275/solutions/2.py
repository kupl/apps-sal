(N, K) = map(int, input().split())


def cnt(n):
    if n < 2:
        return 0
    if n > 2 * N:
        return 0
    return n - 2 * max(n - N, 1) + 1


ans = 0
for ab in range(2, 2 * N + 1):
    cd = ab - K
    ans += cnt(ab) * cnt(cd)
print(ans)
