from collections import Counter


def solve(string):
    n, *aqbc = list(map(int, string.split()))
    a, _, bc = aqbc[:n], aqbc[n], aqbc[n + 1:]
    s = sum(a)
    t = Counter(a)
    ans = []
    for b, c in zip(*[iter(bc)] * 2):
        s += (c - b) * t[b]
        t[c] += t[b]
        t[b] = 0
        ans.append(s)
    return "\n".join(map(str, ans))


def __starting_point():
    import sys
    print((solve(sys.stdin.read().strip())))


__starting_point()
