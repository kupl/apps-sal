import sys
import os

def solve(n, k, h):
    h.sort()
    top = h[len(h) - 1]

    s = [n] * top
    c = 0
    for i in range(top):
        s[i] = n - c
        while c < n and h[c] == i + 1:
            c += 1

    pack = 0
    result = 0
    c = top - 1
    while s[c] < n:
        diff = s[c]
        c -= 1

        if pack + diff <= k:
            pack += diff
        else:
            pack = diff
            result += 1

    if pack > 0:
        result += 1

    return result



def main():
    n, k = (int(x) for x in input().split())
    h = list(int(x) for x in input().split())
    print(solve(n, k, h))

def __starting_point():
    main()
__starting_point()
