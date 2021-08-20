(n, m) = list(map(int, input().split()))
d = {}
for i in range(m):
    (a, b) = list(map(int, input().split()))
    if a not in d:
        d[a] = {b}
    else:
        d[a].add(b)
    if b not in d:
        d[b] = {a}
    else:
        d[b].add(a)
not_visited = set(range(2, n + 1))
visited = set()
current = set()
stack = [1]
succ = True
while len(visited) < n:
    if not stack:
        t = not_visited.pop()
        stack = [t]
        current = set()
    p = stack.pop()
    visited.add(p)
    if p in d:
        for y in current:
            if y not in d[p]:
                succ = False
                break
        if not succ:
            break
        current.add(p)
        for x in d[p]:
            if x in not_visited:
                stack.append(x)
                not_visited.remove(x)
if succ:
    print('YES')
else:
    print('NO')
