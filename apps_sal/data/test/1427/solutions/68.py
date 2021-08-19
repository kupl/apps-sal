from math import gcd
n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
cm = 1
for i in range(n):
    cm = cm * a[i] // gcd(cm, a[i])
ai = sum((pow(x, mod - 2, mod) for x in a))
print(int(ai * cm % mod))
