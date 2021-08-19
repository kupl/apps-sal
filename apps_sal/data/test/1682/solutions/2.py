(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted([(a[i] - b[i], a[i], b[i]) for i in range(n)])
total = 0
for e in c[:k]:
    total += e[1]
for e in c[k:]:
    total += min(e[1], e[2])
print(total)
