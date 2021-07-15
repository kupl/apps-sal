"""http://codeforces.com/problemset/problem/342/B"""

def solve(s, f, t):
    res = ''
    step = 1 if s < f else -1
    i = current = 0
    while s != f:
        current += 1
        ti, l, r = t[i] if i < len(t) else (-1, -1, -1)
        if ti == current:
            i += 1
            if l <= s <= r or l <= s + step <= r:
                res += 'X'
                continue
        s += step
        res += 'R' if step > 0 else 'L'
    return res

def __starting_point():
    parse = lambda: list(map(int, input().split()))
    n, m, s, f = parse()
    l = [parse() for _ in range(m)]
    print(solve(s, f, l))

__starting_point()
