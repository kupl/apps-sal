import sys
sys.setrecursionlimit(100000)


def func(n):
    if n == 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    res = n
    for i in range(1, n + 1):
        pow6 = 6 ** i
        if pow6 > n:
            break
        res = min(res, func(n - pow6) + 1)
    for i in range(1, n + 1):
        pow9 = 9 ** i
        if pow9 > n:
            break
        res = min(res, func(n - pow9) + 1)
    memo[n] = res
    return res


N = int(input())
max_n = 110000
memo = [-1] * max_n
ans = func(N)
print(ans)
