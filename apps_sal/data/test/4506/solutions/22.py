IN = input


def rint():
    return int(IN())


def rmint():
    return map(int, IN().split())


def rlist():
    return list(rmint())


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
