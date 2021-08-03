import numpy as np

N = int(input())
A = list(map(int, input().split()))

ans = 0


def func1(n):
    return n / 2


def func2(n):
    return n % 2


i = 0
while i == 0:

    x = list(map(func2, A))

    if sum(x) == 0:
        ans += 1
        A = list(map(func1, A))
    else:
        break

print(ans)
