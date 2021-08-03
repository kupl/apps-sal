n, *l = map(int, open(0).read().split())
ans = 0
l.sort()
for i in range(n):
    for j in range(i):
        for k in range(j):
            if l[k] == l[j] or l[j] == l[i]:
                continue
            if l[k] + l[j] > l[i]:
                ans += 1
print(ans)
