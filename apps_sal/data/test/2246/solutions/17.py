n = int(input())

tree = {x: [] for x in range(1, n + 1)}

for _ in range(n - 1):
    k, l = list(map(int, input().split()))
    tree[k].append(l)
    tree[l].append(k)


visited = set()
s = 0

a = [(1, 1, 0)]

while a:
    v, p, l = a.pop()
    visited.add(v)
    k = 0
    for vv in tree[v]:
        if vv not in visited:
            k += 1
    if k <= 0:
        s += p * l
    else:
        for vv in tree[v]:
            if vv not in visited:
                a.append((vv, p * 1.0 / k, l + 1))

print(s)
