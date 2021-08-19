import sys
inf = 1 << 30


def solve():
    n = int(input())
    a = [0] + [int(i) for i in input().split()]
    maxi = max(a)
    f = [-1] * (maxi + 1)
    for i in range(1, n + 1):
        if f[a[i]] == -1:
            f[a[i]] = i
    l = [-1] * (maxi + 1)
    for i in range(n, 0, -1):
        if l[a[i]] == -1:
            l[a[i]] = i
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i == l[a[i]]:
            min_l = f[a[i]]
            max_r = i
            used = set()
            v = 0
            for j in range(i, -1, -1):
                min_l = min(min_l, f[a[j]])
                max_r = max(max_r, l[a[j]])
                if a[j] not in used:
                    v ^= a[j]
                    used.add(a[j])
                if max_r > i:
                    break
                if j == min_l:
                    dp[i] = max(dp[i], dp[j - 1] + v)
                    break
    ans = dp[n]
    print(ans)


def __starting_point():
    solve()


__starting_point()
