#!/usr/bin/env python3

def m(k, a):
    if (k == 1):
        return min(a)
    elif (k == 2):
        return max(a[0], a[-1])
    else:
        return max(a)

def __starting_point():
    _, k = list(map(int, input().split()))
    print(m(k, list(map(int, input().split()))))

__starting_point()
