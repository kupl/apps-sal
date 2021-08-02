def R(): return list(map(int, input().split()))


n, l, r = R()
a, d = list(R()), list(R())
b = [l for _ in range(n)]
c = [0 for _ in range(n)]
for i in range(n):
    c[d[i] - 1] = i
dif = l - a[c[0]]
for x in c[1:]:
    if b[x] - a[x] <= dif:
        b[x] = a[x] + dif + 1
    dif = b[x] - a[x]
    if b[x] > r:
        print("-1")
        return
print(" ".join(map(str, b)))
