(n, k) = list(map(int, input().split()))
ar = list(map(int, input().split()))
cross = [0] * n
res = [0] * n
nar = list(sorted([[ar[x], x] for x in range(n)]))
cur = ['1', 0]
for x in nar:
    if x[0] == cur[0]:
        cur[1] += 1
        cross[x[1]] += cur[1]
    else:
        cur[0] = x[0]
        cur[1] = 0
for x in range(k):
    (a, b) = [int(x) - 1 for x in input().split()]
    if ar[a] != ar[b]:
        cross[max(a, b, key=lambda x: ar[x])] += 1
for x in range(n):
    res[x] -= cross[x]
    res[nar[x][1]] += x
print(*res)
