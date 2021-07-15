mod = 10 ** 9 + 7

N = int(input())

memo = {0:1, 1:2}
def f(n):
    if n not in memo:
        memo[n] = (f(n // 2) + f((n - 1) // 2) + f((n - 2) // 2)) % mod
    return memo[n]

print(f(N))
