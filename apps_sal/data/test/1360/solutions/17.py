#!/usr/bin/env python3

def rl(T=str):
    return list(map(T, input().split()))


def main():
    n, = rl(int)
    rec = []
    for _ in range(n):
        rec.append(rl(int))

    rec.sort()

    d = 0
    for a, b in rec:
        if d <= b:
            d = b
        else:
            d = a

    print(d)


main()
