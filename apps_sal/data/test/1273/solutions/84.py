from collections import deque

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]

l = [[] for _ in range(n+1)]
for a, b in ab:
    l[a].append(b)
    l[b].append(a)

parents = [-1] * (n+1)
order = []
q = deque()
q.append(1)
while q:
    c = q.pop()
    order.append(c)
    for i in l[c]:
        if i == parents[c]:
            continue
        parents[i] = c
        q.append(i)

color = [-1] * (n+1)
for i in order:
    ng = color[i]
    c = 1
    for j in l[i]:
        if j == parents[i]:
            continue
        if c == ng:
            c += 1
        color[j] = c
        c += 1

ans = []
for a, b in ab:
    if a == parents[b]:
        ans.append(color[b])
    else:
        ans.append(color[a])

print((max(ans)))
print(('\n'.join(list(map(str, ans)))))

