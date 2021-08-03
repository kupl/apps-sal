n, m = map(int, input().split())
a = list(map(int, input().split()))
f = [[] for i in range(m)]
l = [0 for i in range(m)]
for i in range(n):
    f[a[i] % m].append(i)
    l[a[i] % m] += 1
k = n // m
j = 0
tot = 0
for i in range(m):
    while l[i] > k:
        while l[j] >= k:
            j = (j + 1) % m
        tot += (j + m - i) % m
        l[j] += 1
        a[f[i][-1]] += (j + m - i) % m
        f[i].pop()
        l[i] -= 1
    if i == j:
        j += 1
print(tot)
for i in a:
    print(i, end=' ')
