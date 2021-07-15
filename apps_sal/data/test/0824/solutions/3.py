t = input()
n, m = len(t) + 1, 1000000007
a, b = 0, t.count(')') - 1
f = [1] * n
for i in range(2, n): f[i] = i * f[i - 1] % m
g = [pow(q, m - 2, m) for q in f]
s = 0
for q in t:
    if b < 0: break
    if q == '(':
        a += 1
        s += f[a + b] * g[a] * g[b]
    else: b -= 1
print(s % m)
