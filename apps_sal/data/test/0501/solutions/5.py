mod = 10 ** 9 + 7


def f(n):
    v = [1, 2]
    cnt = 1
    all = 0
    ans = 0
    while (all < n):
        cnt = min(cnt, n - all)
        all += cnt
        ans += (2 * v[0] + (cnt - 1) * 2) * cnt // 2
        ans %= mod
        v[0] += cnt * 2
        cnt *= 2
        v[0], v[1] = v[1], v[0]
    return ans


l, r = list(map(int, input().split()))
print((f(r) - f(l - 1) + mod * mod) % mod)
