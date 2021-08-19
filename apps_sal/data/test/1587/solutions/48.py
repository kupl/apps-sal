def solve(string):
    (n, c) = string.split()
    (n, c) = (int(n), list(c))
    (wi, ri) = (0, n - 1)
    while wi < n and c[wi] == 'R':
        wi += 1
    while ri >= 0 and c[ri] == 'W':
        ri -= 1
    ans = 0
    while wi < n and ri >= 0 and (wi < ri):
        (c[wi], c[ri], ans) = (c[ri], c[wi], ans + 1)
        (wi, ri) = (wi + 1, ri - 1)
        while wi < n and c[wi] == 'R':
            wi += 1
        while ri >= 0 and c[ri] == 'W':
            ri -= 1
    return str(ans)


def __starting_point():
    import sys
    print(solve(sys.stdin.read().strip()))


__starting_point()
