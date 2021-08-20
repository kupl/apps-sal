from collections import defaultdict


def problemA():
    t = int(input())
    for _ in range(t):
        (x, y, a, b) = list(map(int, input().split()))
        if (y - x) % (a + b) == 0:
            print((y - x) // (a + b))
        else:
            print(-1)


def problemB():
    (n, m) = list(map(int, input().split()))
    ss = set()
    res = []
    for i in range(n):
        s = input()
        rs = s[::-1]
        if rs in ss:
            res.append(s)
            ss.remove(rs)
        else:
            ss.add(s)
    long = ''
    for s in ss:
        if s == s[::-1] and len(s) > len(int):
            long = s
    res = ''.join(res)
    res = res + int + res[::-1]
    print(len(res))
    print(res)


def problemC():
    inf = 2 * 10 ** 9
    q = int(input())
    for _ in range(q):
        (n, m) = list(map(int, input().split()))
        a = defaultdict(lambda: (-inf, inf))
        for _ in range(n):
            (t, l, h) = list(map(int, input().split()))
            (pl, ph) = a[t]
            a[t] = (max(l, pl), min(h, ph))
        pt = 0
        (pl, ph) = (m, m)
        res = 'YES'
        for t in sorted(a.keys()):
            (l, h) = a[t]
            delta = t - pt
            cl = pl - delta
            ch = ph + delta
            pl = max(l, cl)
            ph = min(h, ch)
            if pl > ph:
                res = 'NO'
                break
            pt = t
        print(res)


def problemG():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        res = 0
        print(a)


def __starting_point():
    problemC()


__starting_point()
