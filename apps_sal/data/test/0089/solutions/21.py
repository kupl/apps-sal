n = int(input())

memo = dict()


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    memo[n] = n + f(n - 2)
    return memo[n]


print(f(n))
