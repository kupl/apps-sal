from math import factorial

n, m = map(int, input().split())
if n == m:
    ans = factorial(n) % (10 ** 9 + 7)
    ans = ans ** 2 % (10 ** 9 + 7)
    print(ans * 2 % (10 ** 9 + 7))
elif abs(n - m) == 1:
    ans1 = factorial(n) % (10 ** 9 + 7)
    ans2 = factorial(m) % (10 ** 9 + 7)
    print(ans1 * ans2 % (10 ** 9 + 7))
else:
    print(0)
