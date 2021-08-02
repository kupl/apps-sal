n, k = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n - 1)]
mod = 10 ** 9 + 7

adj = [[] for _ in range(n + 1)]
for a, b in ab:
    adj[a].append(b)
    adj[b].append(a)

s = 1
p = [-1] * (n + 1)
p[0] = 0
p[1] = 0
c = [[] for _ in range(n + 1)]
order = []
stack = [s]
while stack:
    u = stack.pop()
    order.append(u)
    for v in adj[u]:
        if p[v] == -1:
            p[v] = u
            c[u].append(v)
            stack.append(v)

ans = k
for u in order:
    mx = k - 1
    par = p[u]
    if par:
        mx -= 1

    for i in range(len(c[u])):
        ans *= mx - i
        ans %= mod

print(ans)
