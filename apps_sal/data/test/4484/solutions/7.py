from math import factorial

n, m = map(int, input().split())
if n == m:
    print((factorial(n) ** 2 * 2) % (10 ** 9 + 7))
elif abs(n - m) == 1:
    print((factorial(n) * factorial(m)) % (10 ** 9 + 7))
else:
    print(0)
