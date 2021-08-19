n = int(input())

children = [[] for _ in range(n)]
ps = [int(v) for v in input().split()]

for i, p in enumerate(ps, 1):
    children[p - 1].append(i)

cs = [int(v) for v in input().split()]

ans = 0

# vertex, color
stack = [(0, 0)]
while stack:
    v, c = stack.pop()
    if c != cs[v]:
        ans += 1
        c = cs[v]
    for child in children[v]:
        stack.append((child, c))

print(ans)
