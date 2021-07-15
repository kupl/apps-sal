# -*- coding: utf-8 -*-
import math


def binary(n):
    lst = []
    while n != 0:
        lst.append(n % 2)
        n = n // 2
    lst = lst + [0] * (31 - len(lst))
    return list(reversed(lst))


def calc(u, v):
    result = ""
    u_binary = binary(u)
    v_binary = binary(v)
    for i in range(31):
        if u_binary[i] == 1 and v_binary[i] == 1:
            result += "R"
        elif u_binary[i] == 0 and v_binary[i] == 0:
            result += "L"
        elif u_binary[i] == 1 and v_binary[i] == 0:
            result += "U"
        else:
            result += "D"
    return result


U = []
V = []
N = int(input())
even, odd = 0, 0

for p in range(N):
    x, y = list(map(int, input().split()))
    U.append(x+y)
    V.append(x-y)
    if (x + y) % 2 == 0:
        even += 1
    else:
        odd += 1

if even >= 1 and odd >= 1:
    print((-1))

else:
    lst = [2 ** i for i in range(30, -1, -1)]
    if odd == 0:
        lst.append(1)
    print((len(lst)))
    print((" ".join(map(str, lst))))
    for u, v in zip(U, V):
        u = (u + 2 ** 31 - 1) // 2
        v = (v + 2 ** 31 - 1) // 2
        print((calc(u, v)+"R" if odd == 0 else calc(u, v)))

