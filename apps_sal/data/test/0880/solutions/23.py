n = int(input())

M = 998244353
f = n
s = n
for i in range(1, n):
    f = f * (n - i)
    x = n - i - 1
    y = (f * x) // (x + 1)
    s += (i + 1) * y
    s %= M
    f %= M
print(s % M)

