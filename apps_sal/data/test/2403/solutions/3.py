n = int(input())

a = list(map(int, input().split()))
b = list(int(x) - 1 for x in input().split())

indeg = [0] * n
for x in b:
    if x >= 0:
        indeg[x] += 1
q = [i for i in range(n) if indeg[i] == 0]
ans = 0
res = []
end = []
while q:
    top = q.pop()
    if a[top] < 0:
        end.append(top)
    else:
        res.append(top)
        ans += a[top]
        if b[top] >= 0:
            a[b[top]] += a[top]
    if b[top] >= 0:
        nei = b[top]
        indeg[nei] -= 1
        if indeg[nei] == 0:
            q.append(nei)

for i in end[::-1]:
    ans += a[i]
    if b[i] >= 0:
        a[b[i]] += a[i]
    res.append(i)

print(ans)
print(*[x + 1 for x in res])
