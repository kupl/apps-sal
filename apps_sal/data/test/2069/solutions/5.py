def solver():
    import sys
    it = (int(x) for line in sys.stdin.read().splitlines() for x in line.split(' '))
    (n, m) = (next(it), next(it))
    revp = [0] * (n + 1)
    for i in range(n):
        revp[next(it)] = i
    pairs = [-1] * (n + 1)
    pairs[-1] = n - 1
    for _ in range(m):
        (a, b) = (next(it), next(it))
        (a, b) = (revp[a], revp[b])
        if b > a:
            (a, b) = (b, a)
        pairs[a] = max(pairs[a], b)
    res = 0
    pos = 0
    for (right, left) in enumerate(pairs):
        if left == -1:
            continue
        for i in range(pos, left + 1):
            res = res + right - i
        pos = max(pos, left + 1)
    return res


def main():
    import sys
    res = solver()
    sys.stdout.write('{}\n'.format(res))
    return 0


def __starting_point():
    main()


__starting_point()
