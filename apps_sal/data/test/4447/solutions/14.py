from collections import defaultdict
(n, m) = map(int, input().split())
k = n // m
l = list(map(int, input().split()))
s = sum(l)
occ = defaultdict(list)
for (i, a) in enumerate(l):
    rem = a % m
    occ[rem].append(i)
j = 0
for i in range(m):
    while len(occ[i]) > k:
        while j < i or len(occ[j % m]) >= k:
            j += 1
        key = occ[i].pop()
        l[key] += (j - i) % m
        occ[j % m].append(k)
print(sum(l) - s)
print(*l)
