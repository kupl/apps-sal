from math import gcd
x = int(input())
ans = 10 ** 18
for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
        if gcd(i, x // i) == 1:
            if max(i, x // i) < ans:
                ans = max(i, x // i)
                w = [i, x // i]
print(*w)
