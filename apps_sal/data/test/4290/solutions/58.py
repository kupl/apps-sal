import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


(n, m) = list(map(int, input().split()))
if n <= 1 and m <= 1:
    ans = 0
elif n <= 1:
    ans = comb(m, 2)
elif m <= 1:
    ans = comb(n, 2)
else:
    ans = comb(n, 2) + comb(m, 2)
print(ans)
