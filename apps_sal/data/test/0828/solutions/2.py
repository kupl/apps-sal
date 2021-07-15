f = lambda: map(int, input().split())
n, s = f()
c = [0] * n
t = list(f())
for i in t: c[i] += 1
k = t[s - 1]
c[k] -= 1
d = c[0]
c += [d]
d += k > 0
i, j = 1, n
while i < j:
    if c[i]: i += 1
    elif c[j]:
        c[j] -= 1
        i += 1
        d += j < n
    else: j -= 1
print(d)
