import math
(n, m) = map(int, input().split())
if abs(n - m) >= 2:
    print(0)
elif abs(n - m) == 1:
    ans = math.factorial(n) * math.factorial(m)
    ans %= 10 ** 9 + 7
    print(ans)
else:
    ans = 2 * math.factorial(n) * math.factorial(m)
    ans %= 10 ** 9 + 7
    print(ans)
