import math
n, m = list(map(int, input().split()))
if abs(n - m) > 1:
    print((0))
elif abs(n - m) == 1:
    print(((math.factorial(n) * math.factorial(m)) % (10**9 + 7)))
else:
    print(((2 * math.factorial(n) * math.factorial(m)) % (10**9 + 7)))
