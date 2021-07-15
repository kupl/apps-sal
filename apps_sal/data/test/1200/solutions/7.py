from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(1, len(a)):
    a[i-1] = a[i] - a[i-1]
a.pop()
g = a[0]
s = 0
for i in range(len(a)):
    s += a[i]
    g = gcd(g, a[i])
s = s // g - len(a)
print(s)
