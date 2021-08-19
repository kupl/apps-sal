(k, n) = map(int, input().split())
a = list(map(int, input().split()))
d = []
for i in range(n - 1):
    d.append(a[i + 1] - a[i])
d.append(k - a[n - 1] + a[0])
d.sort()
print(sum(d[:-1]))
