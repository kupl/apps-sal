n, m = list(map(int, input().split()))

import math
if n == m:
    dog = math.factorial(n)
    mon = math.factorial(m)
    ans = dog * mon * 2
elif n == m + 1 or n == m - 1:
    dog = math.factorial(n)
    mon = math.factorial(m)
    ans = dog * mon
else:
    ans = 0

print((ans % (10 ** 9 + 7)))

