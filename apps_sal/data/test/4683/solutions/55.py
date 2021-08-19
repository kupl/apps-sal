import sys
n = int(input())
a = [int(x) for x in input().split()]
s = 0
for i in range(n):
    s += a[i]
c = 0
sum = 0
for k in range(n - 1):
    c += a[k]
    co = s - c
    sum += a[k] * co
print(sum % (10 ** 9 + 7))
