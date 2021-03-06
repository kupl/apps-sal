def solve(N, K, x):
    l = [abs(xi) for xi in x if xi < 0] + [0]
    l.reverse()
    r = [0] + [xi for xi in x if xi >= 0]
    ans = 10 ** 18 * 2 + 1
    for i in range(max(K - (len(l) - 1), 0), min(K + 1, len(r))):
        ll = l[K - i]
        rr = r[i]
        ans = min(ans, min(ll, rr) * 2 + max(ll, rr))
    print(ans)


def __starting_point():
    (N, K) = list(map(int, input().split()))
    x = [int(i) for i in input().split()]
    solve(N, K, x)


__starting_point()
