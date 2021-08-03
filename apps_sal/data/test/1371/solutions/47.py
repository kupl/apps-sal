import math


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n = int(input())
s = n // 3
a = 0
if(s >= 1):
    for i in range(1, s + 1):
        t = n - 3 * i
        a += C(t + i - 1, i - 1)
    print((a % 1000000007))
else:
    print((0))
