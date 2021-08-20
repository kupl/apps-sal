from math import sqrt, factorial
from sys import setrecursionlimit
setrecursionlimit(10000000)


def inpl():
    return list(map(int, input().split()))


N = int(input())
S = int(input())
RN = int(sqrt(N)) + 1
RN += (RN + 1) ** 2 == N


def func(b, N):
    if b <= 1:
        return -1
    tmp = 0
    while N:
        (N, d) = divmod(N, b)
        tmp += d
    return tmp


for b in range(2, RN + 1):
    tmp = func(b, N)
    if tmp == S:
        print(b)
        break
else:
    for x in range(RN, 0, -1):
        b = (N - S + x) // x
        if func(b, N) == S:
            print(b)
            break
    else:
        if func(S + 1, N) == S:
            print(S + 1)
        else:
            print(-1)
