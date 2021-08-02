from collections import Counter


def main():
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    p = l.index(m)
    le, ri = Counter(), Counter()
    c = 0
    le[0] = ri[0] = 1
    for i in range(p + 1, n):
        if l[i] < m:
            c += 1
        else:
            c -= 1
        ri[c] += 1
    c = 0
    for i in range(p - 1, -1, -1):
        if l[i] < m:
            c -= 1
        else:
            c += 1
        le[c] += 1
    res = 0
    for c, x in list(le.items()):
        res += x * (ri[c] + ri[c - 1])
    print(res)


def __starting_point():
    main()


__starting_point()
