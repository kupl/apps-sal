from collections import Counter
n, a, b = int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()]
c = Counter(b)
nex = list(range(1, n)) + [0]
ans = []
for i in a:
    v = (n - i) % n
    while c[v] == 0:
        if c[nex[v]] == 0:
            nex[v] = nex[nex[v]]
        v = nex[v]
    c[v] -= 1
    ans.append((i + v) % n)
print(*ans)
