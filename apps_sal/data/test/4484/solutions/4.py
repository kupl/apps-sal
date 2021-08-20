import math
(n, m) = map(int, input().split())
r = 10 ** 9 + 7
if n == m:
    print(2 * math.factorial(n) * math.factorial(m) % r)
elif abs(n - m) == 1:
    print(math.factorial(n) * math.factorial(m) % r)
else:
    print(0)
