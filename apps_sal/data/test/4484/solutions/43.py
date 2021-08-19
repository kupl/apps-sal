import math
(n, m) = list(map(int, input().split()))
if abs(n - m) >= 2:
    print(0)
elif n == m:
    print(2 * math.factorial(n) * math.factorial(m) % (10 ** 9 + 7))
else:
    print(math.factorial(n) * math.factorial(m) % (10 ** 9 + 7))
