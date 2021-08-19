from sys import stdin
lines = list([_f for _f in stdin.read().split('\n') if _f])


def parseline(line):
    return list(map(int, line.split()))


lines = list(map(parseline, lines))


def search(f, v, l, r):
    while l + 1 < r:
        p = l + (r - l) // 2
        if f(p) <= v:
            l = p
        else:
            r = p
    return l


c1, c2, x, y = lines[0]


def check(v, debug=False):
    m1 = max(c1 - v // y + v // (x * y), 0)
    m2 = max(c2 - v // x + v // (x * y), 0)
    f = v - v // x - v // y + v // (x * y)
    if debug:
        print(v, ":", m1, m2, f)
    if m2 <= f - m1:
        return 1
    else:
        return 0


#print([check(v, True) for v in range(20)])
print(1 + search(check, 0, 1, y * c1 + x * c2 + 1))
