from sys import stdin
input = stdin.readline
inf = 1000 * 1000 * 1000
(n, k) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = []
for i in range(200001):
    b.append([])
for i in a:
    ctr = 0
    while i > 0:
        b[i].append(ctr)
        i //= 2
        ctr += 1
    b[i].append(ctr)
res = inf
for i in b:
    if len(i) >= k:
        i.sort()
        tmp = 0
        for j in range(k):
            tmp += i[j]
        res = min(res, tmp)
print(res)
