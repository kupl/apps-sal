(n, q) = list(map(int, input().split()))
g = [[] for i in range(n + 1)]
p = list(map(int, input().split()))
for i in range(n - 1):
    g[p[i]].append(i + 2)
timer = 0
children = [0] * (n + 1)
when = [0] * (n + 1)
a = []
instack = [0] * (n + 1)
stack = [1]
while stack:
    u = stack[-1]
    if instack[u] == 1:
        children[u] = len(a) - when[u]
        stack.pop()
        continue
    a.append(u)
    when[u] = len(a) - 1
    instack[u] = 1
    for i in reversed(g[u]):
        stack.append(i)
ans = [0] * q
for i in range(q):
    (x, y) = list(map(int, input().split()))
    y -= 1
    ans[i] = '-1' if y >= children[x] else str(a[when[x] + y])
print('\n'.join(ans))
