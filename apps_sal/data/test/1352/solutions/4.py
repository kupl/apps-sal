import os
from io import BytesIO, StringIO


def input_as_list():
    return list(map(int, input().split()))


def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()


def main():
    (n, x) = input_as_list()
    a = input_as_list()
    fo = array_of(lambda: -1, x + 1)
    lo = array_of(lambda: -1, x + 1)
    ans = 0
    for (i, e) in enumerate(a):
        if fo[e] == -1:
            fo[e] = i
        lo[e] = i
    lastidx = -1
    for i in range(1, x + 1):
        if fo[i] != -1:
            if lastidx < fo[i]:
                lastidx = lo[i]
            else:
                i -= 1
                break
    L = i
    firstidx = n + 1
    for i in range(x, 0, -1):
        if fo[i] != -1:
            if lo[i] < firstidx:
                firstidx = fo[i]
            else:
                i += 1
                break
    R = i
    ans += min(x - R + 2, x)
    c = n
    for i in range(x, R - 1, -1):
        if fo[i] == -1:
            fo[i] = c
        else:
            c = fo[i]
    r = R
    l = 1
    while l <= L:
        if l + 1 < r and (lo[l] == -1 or x < r or lo[l] < fo[r]):
            ans += x - r + 2
            l += 1
        else:
            r += 1
    print(ans)


main()
