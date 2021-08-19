#!/usr/bin/env python3

def main():
    a, b, c = [int(x) for x in input().split()]
    if a == b:
        print('YES')
    elif c == 0:
        print('YES' if (b == a) else 'NO')
    else:
        n = (b - a) // abs(c)
        x = (b - a) % abs(c)
        print('YES' if x == 0 and n * c > 0 else 'NO')


def __starting_point():
    main()


__starting_point()
