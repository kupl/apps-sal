from fractions import gcd
m = -1
a = -1
b = 1
n = int(input())
for i in range(n // 2, -1, -1):
    if gcd(i, n - i) == 1 and i != n - i:
        if i / (n - i) > m:
            m = i / (n - i)
            a = i
            b = n - i
print(a, b)
