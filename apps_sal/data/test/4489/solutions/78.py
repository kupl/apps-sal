#!/usr/bin/env python3


def main():
    N = int(input())
    s = [input() for _ in range(N)]
    M = int(input())
    t = [input() for _ in range(M)]
    y = 0
    for ss in set(s):
        yy = s.count(ss) - t.count(ss)
        if y < yy:
            y = yy
    print(y)


main()
