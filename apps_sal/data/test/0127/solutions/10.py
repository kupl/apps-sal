(n, f) = list(map(int, input().split()))
a = []
for _ in range(n):
    (k, l) = list(map(int, input().split()))
    a.append((-(min(l, k * 2) - min(l, k)), min(l, k)))
a.sort()
tot = 0
for i in range(0, f):
    tot += -a[i][0] + a[i][1]
for i in range(f, n):
    tot += a[i][1]
print(tot)
