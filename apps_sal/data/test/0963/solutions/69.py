def main():
    n, k = map(int, input().split())
    mod = 998244353
    s = [list(map(int, input().split()))]
    for _ in range(k - 1):
        l, r = map(int, input().split())
        s.append([l, r])
    ans = [0] * (n + 1)
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = -1
    for i in range(1, n + 1):
        ans[i] += (ans[i - 1] + d[i]) % mod
        for l, r in s:
            if i + l < n + 1:
                d[i + l] += ans[i] % mod
            if i + r + 1 < n + 1:
                d[i + r + 1] -= ans[i] % mod
    print(ans[-1] % mod)


def __starting_point():
    main()


__starting_point()
