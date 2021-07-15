f = lambda: map(int, input().split())
n, m, k = f()
t = sorted(f())
d = [1] * n
i = s = 0
for j in range(n):
    while t[j] - t[i] >= m:
        k += d[i]
        i += 1
    k -= 1
    if k < 1:
        s += 1
        k = 1
        d[j] = 0
print(s)
