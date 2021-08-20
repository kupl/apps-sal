from collections import deque
(n, m) = tuple(map(int, input().split()))
l = [0] + list(map(int, input().split()))
graph = [set() for i in range(n + 1)]
for i in range(n - 1):
    (a, b) = tuple(map(int, input().split()))
    graph[a].add(b)
    graph[b].add(a)
maxcats = [0] * (n + 1)
cats = [0] * (n + 1)
checked = [0] * (n + 1)
q = deque()
q.append((1, 0, 0))
res = 0
while len(q) > 0:
    ij = q.popleft()
    i = ij[0]
    j = ij[1]
    maxi = ij[2]
    checked[i] = 1
    if l[i]:
        j += 1
    else:
        j = 0
    if maxi < j:
        maxi = j
    islist = 1
    for elem in graph[i]:
        if not checked[elem]:
            q.append((elem, j, maxi))
            islist = 0
    if islist:
        if maxi <= m:
            res += 1
print(res)
