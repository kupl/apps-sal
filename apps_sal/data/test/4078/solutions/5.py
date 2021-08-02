n, m = list(map(int, input().split()))
b = list(map(int, input().split()))
se = []
for i in range(m):
    se.append(list(map(int, input().split())))
k = max(b) - min(b)
ans = []
for i in range(n):
    l = []
    r = b[:]
    for j in range(m):
        c, d = se[j][0], se[j][1]
        if i not in list(range(c - 1, d)):
            for x in range(c - 1, d):
                r[x] -= 1
            l.append(j + 1)
    x = max(r) - min(r)
    if x > k:
        k = x
        ans = l
print(k)
print(len(ans))
print(*ans)
