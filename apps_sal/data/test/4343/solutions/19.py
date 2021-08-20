import os
import io


def arr(ls):
    l = [0] * len(ls)
    for (i, v) in enumerate(ls):
        l[i] = ord(v) - 97
    return l


def div2(ls, n):
    carry = 0
    for i in range(n):
        rem = ls[i] % 2 == 1
        ls[i] = ls[i] // 2 + carry
        if rem:
            carry = 13
        else:
            carry = 0
    return ls


def subtr(ls1, ls2, n):
    carry = 0
    for i in range(n - 1, -1, -1):
        ls1[i] -= carry
        carry = int(ls1[i] < ls2[i])
        ls1[i] = (ls1[i] - ls2[i]) % 26
    return ls1


def add(ls1, ls2, n):
    for i in range(n - 1, -1, -1):
        ls1[i] += ls2[i]
        if ls1[i] > 25:
            ls1[i - 1] += 1
            ls1[i] -= 26
    return ls1


def kk():
    return list(map(int, input().split()))


def k2():
    return [int(x) - 1 for x in input().split()]


def ll():
    return list(kk())


(n, w1, w2) = (int(input()), list(input().strip()), list(input().strip()))
(ls1, ls2) = (arr(w1), arr(w2))
subtr(ls2, ls1, n)
div2(ls2, n)
add(ls1, ls2, n)
print(''.join([chr(97 + x) for x in [x for x in ls1]]))
