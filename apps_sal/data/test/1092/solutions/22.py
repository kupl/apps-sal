(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
l1 = []
l1.append(l[0] - 1)
for i in range(m - 1):
    l1.append(l[i + 1] - l[i] - 1)
f1 = [1] * 1001
f2 = [1] * 1001
mod = 10 ** 9 + 7
a = 1
b = 1
for i in range(1, 1001):
    a *= i
    a %= mod
    f1[i] = a
    b *= pow(i, mod - 2, mod)
    b %= mod
    f2[i] = b
ans = 1
n -= m
ans *= f1[n] * f2[l1[0]] * f2[n - l1[0]]
ans %= mod
n -= l1[0]
for i in range(1, len(l1)):
    if l1[i] > 0:
        ans *= f1[n] * f2[l1[i]] * f2[n - l1[i]] * pow(2, l1[i] - 1, mod)
        ans %= mod
        n -= l1[i]
print(ans)
