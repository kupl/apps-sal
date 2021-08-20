(n, a) = (int(input()), list(map(int, input().split())))
(r, i, x) = (0, 0, 0)
for j in range(n):
    while x < n and i & a[x] == 0:
        i += a[x]
        x += 1
    r += x - j
    i -= a[j]
print(r)
