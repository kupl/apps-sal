from math import *


def Main(n):
    sm = 0
    A = []
    for i in range(1, n + 1):
        sm += i
        A.append(i)
        if sum(A) == n:
            break
        elif sum(A) > n:
            break
    rez = abs(n - sum(A))
    if rez in A:
        value_index = A.index(rez)
        A.pop(value_index)
    print(len(A))
    print(*A)


def __starting_point():
    n = int(input())
    Main(n)


__starting_point()
