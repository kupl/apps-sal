from collections import defaultdict
n = int(input())

E = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    E[a].append(b)
    E[b].append(a)

stack = [1]
visited = {1}
c = 0
d = 0

turn = True

while stack:
    nstack = []
    for v in stack:
        for u in E[v]:
            if u not in visited:
                nstack.append(u)
                visited.add(u)

    if turn:
        d += len(stack)
    else:
        c += len(stack)
    turn = not turn
    stack = nstack

print(c * d - (n - 1))
