mod = 998244353
n = int(input())
a = [int(i) for i in input().split()]
s = 0
b = ''
for i in range(n):
    s1 = str(a[i])
    b = ''
    for i in range(len(s1)):
        b = b + s1[i] + s1[i]
    s += int(b) % mod
print(s * n % mod)
