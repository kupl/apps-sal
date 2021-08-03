"""http://codeforces.com/problemset/problem/259/B"""


def solve(s):
    rows = list(map(sum, [s[i] for i in range(3)]))
    r = sorted(rows)
    d1 = r[1] - r[0]
    d2 = r[2] - r[1]
    m = 3 * (r[0] - d2) / 2 + 2 * d2 + d1
    m = int(m)
    for i in range(3):
        s[i][i] = m - rows[i]
    return s


def __starting_point():
    res = solve([list(map(int, input().split())) for _ in range(3)])
    for i in range(3):
        print(' '.join(map(str, res[i])))


__starting_point()
