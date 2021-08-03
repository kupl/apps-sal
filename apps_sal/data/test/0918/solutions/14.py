#!/usr/bin/env python3

def read_ints(): return list(map(int, input().split()))


def __starting_point():
    n, m = read_ints()
    R = [[] for _ in range(m)]
    for i in range(n):
        n, r, s = input().split()
        r = int(r)
        s = int(s)
        R[r - 1].append((s, n))

    for r in R:
        r.sort(reverse=True)
        if len(r) > 2:
            if r[1][0] == r[2][0]:
                print("?")
            else:
                print("%s %s" % (r[0][1], r[1][1]))
        else:
            print("%s %s" % (r[0][1], r[1][1]))


__starting_point()
