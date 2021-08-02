def main():
    s = "abcdefghijklmnopqrstuvwxyz"
    d = {(a, b): min((ord(a) - ord(b)) % 26, (ord(b) - ord(a)) % 26) for a in s for b in s}
    n, m = list(map(int, input().split()))
    s, res, n, m = input(), 0, n - 1, min(m - 1, n - m)
    idx = [i for i, a in zip(list(range((n + 1) // 2)), s) if a != s[n - i]]
    print((sum(d[s[i], s[n - i]] for i in idx) + min(abs(m - idx[0]), abs(m - idx[-1])) + idx[-1] - idx[0]) if idx else 0)


def __starting_point():
    main()


__starting_point()
