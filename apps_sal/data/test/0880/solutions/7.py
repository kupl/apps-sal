res = 0
n = int(input())
f = 1
s = 0
for i in range(n, 1, -1):
    f = (f * i) % 998244353
    s = (s + f) % 998244353
print((f * n - s) % 998244353)
