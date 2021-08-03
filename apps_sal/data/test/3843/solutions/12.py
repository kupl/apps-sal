import math


def digits(x, k):
    d = [False] * 7
    for i in range(k):
        if d[x % 7]:
            return False
        d[x % 7] = True
        x //= 7
    return True


def solve(n, m):
    if n * m > 7**7:
        return 0
    k1 = math.ceil(math.log(n, 7)) if n > 1 else 1
    k2 = math.ceil(math.log(m, 7)) if m > 1 else 1
    s = 0
    for i in range(n):
        for j in range(m):
            s += digits(i * 7 ** k2 + j, k1 + k2)
    return s


n, m = list(map(int, input().split()))
print(solve(n, m))
