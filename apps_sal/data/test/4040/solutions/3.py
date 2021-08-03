n, m, d = map(int, input().split())
c = list(map(int, input().split()))
ans = []
s = sum(c)
ind = []
j = -1
for i in range(len(c)):
    v = min(j + d, n - s)
    ind.append(v)
    j = v + c[i] - 1
    s -= c[i]
ans = []
if n - j > d:
    print("NO")
    return
i = 0
j = 0
v = 1
while i < n:
    if j < len(ind) and i == ind[j]:
        for l in range(c[j]):
            ans.append(v)
        v += 1
        i += c[j]
        j += 1
    else:
        i += 1
        ans.append(0)
print("YES")
print(*ans)
