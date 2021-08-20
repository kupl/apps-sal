import numpy as np
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return list(map(int, sys.stdin.readline().split()))


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def main():
    (l, a, b, md) = MI()
    k = 0
    i = 0
    ans = [0, a % md, b % md]
    ans = np.array(ans, dtype='i8')
    while i < l:
        k += 1
        j = (10 ** k - a + b - 1) // b
        if j <= 0:
            continue
        if j > l:
            j = l
        e = j - i
        bb = np.zeros((3, 3), dtype='i8')
        bb[0, 0] = pow(10, k, md)
        bb[1, 0] = bb[1, 1] = bb[2, 1] = bb[2, 2] = 1
        while e:
            if e & 1:
                ans = np.dot(ans, bb) % md
            bb = np.dot(bb, bb) % md
            e >>= 1
        i = j
    print(ans[0])


main()
