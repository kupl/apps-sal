from collections import defaultdict


def main2(n, a, m, b):
    mx = -999
    a.sort()
    b.sort()
    ar = a.copy()
    ar.reverse()
    br = b.copy()
    br.reverse()
    a2 = 0
    b2 = 0
    a3 = n
    b3 = m
    for d in sorted(list(set([0] + a + b))):
        if ar.count(d) > 0:
            a3 = ar.index(d)
        if br.count(d) > 0:
            b3 = br.index(d)
        s1 = (n - a3) * 2 + a3 * 3
        s2 = (m - b3) * 2 + b3 * 3
        if s1 - s2 > mx:
            mx = s1 - s2
            res = "{}:{}".format(s1, s2)
    print(res)


def main(n, a, m, b):
    mx = -99999999999
    a.sort()
    b.sort()
    a2 = 0
    b2 = 0
    for d in sorted(list(set([0] + a + b))):
        for a2 in range(a2, n + 1):
            if a2 == n or a[a2] > d:
                break
        for b2 in range(b2, m + 1):
            if b2 == m or b[b2] > d:
                break
        s1 = a2 * 2 + (n - a2) * 3
        s2 = b2 * 2 + (m - b2) * 3
        if s1 - s2 > mx:
            mx = s1 - s2
            res = "{}:{}".format(s1, s2)
    print(res)


def main_input():
    n = int(input())
    a = [int(i) for i in input().split()]
    m = int(input())
    b = [int(i) for i in input().split()]

    main(n, a, m, b)


def __starting_point():
    main_input()


__starting_point()
