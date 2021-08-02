import math
3


def f(k):
    return int((k * (k - 1) + 2) / 2)


n = int(input())

D = 1 - 4 * (2 - 2 * n)
k = int(math.floor((1 + math.sqrt(D)) / 2))

ans = n - f(k) + 1

print(ans)
