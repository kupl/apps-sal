#!/usr/bin/env python3

def main():
    n, m, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for i in range(m):
        if a[i] > x:
            ans = min(i, len(a) - i)
            break
    else:
        ans = 0
    print(ans)


def __starting_point():
    main()


__starting_point()
