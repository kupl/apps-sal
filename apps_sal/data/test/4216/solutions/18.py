from math import sqrt
n = int(input())
res = 100
for a in range(1, int(sqrt(n)) + 1):
    if n % a == 0:
        b = n // a
        res = min(res, max(len(str(a)), len(str(b))))
print(res)
