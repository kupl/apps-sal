(n, m) = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
l.sort()
best = l[-1] - l[0]
for i in range(len(l) - n + 1):
    cur = l[i + n - 1] - l[i]
    if cur < best:
        best = cur
print(best)
