read = lambda: list(map(int, input().split()))
n, k = read()
a = list(read())
b = list(read())
c = [0] * n
r = [0] * n
for i in range(n):
    c[i] = b[i] // a[i]
    r[i] = a[i] - b[i] % a[i]
while k:
    cur = min(c)
    i = c.index(min(c))
    if k >= r[i]:
        k -= r[i]
        c[i] += 1
        r[i] = a[i]
    else: break
ans = min(c)
print(ans)

