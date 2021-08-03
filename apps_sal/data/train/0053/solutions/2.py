from sys import stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


def p1(n, s, le):
    r = []
    b = i = 0
    while i < n:
        try:
            ni = s.index(le, i) + 1
        except ValueError:
            ni = n
        r += list(range(ni, i, -1))
        i = ni
    return r


t, = rl()
for _ in range(t):
    n, s = stdin.readline().split()
    n = int(n)
    print(*(n - x + 1 for x in p1(n, s, '>')))
    print(*p1(n, s, '<'))
