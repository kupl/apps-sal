IN = input
rint = lambda: int(IN())
rmint = lambda: map(int, IN().split())
rlist = lambda: list(rmint())

n = rint()
a = rlist()
b = rlist()
b.sort()
b.reverse()
for i in range(n):
    a[i] *= (i + 1) * (n - i)
a.sort()
ans = 0
for i in range(n):
    ans += b[i] * a[i]
    ans %= 998244353
print(ans)
