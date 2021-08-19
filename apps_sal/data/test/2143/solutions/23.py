n = int(input())
a = [int(x) for x in input().split()]
d = {}
for i in range(n):
    for j in range(i + 1, n):
        if str(a[i] + a[j]) in d:
            d[str(a[i] + a[j])] += 1
        else:
            d[str(a[i] + a[j])] = 1
m = 0
for i in d:
    if d[i] > m:
        m = d[i]
print(m)
