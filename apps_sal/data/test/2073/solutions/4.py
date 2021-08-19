from sys import stdin
n = int(stdin.readline())
a = [int(x) - 1 for x in stdin.readline().split()]
nodes = set([x for x in range(n)])
loops = []
while nodes:
    for x in nodes:
        nxt = x
        break
    visited = set()
    q = []
    early = False
    while not nxt in visited:
        if not nxt in nodes:
            early = True
            break
        q.append(nxt)
        visited.add(nxt)
        nodes.remove(nxt)
        nxt = a[nxt]
    if not early:
        loops.append(len(q) - q.index(nxt))
base = pow(2, n - sum(loops), 10 ** 9 + 7)
for x in loops:
    base *= pow(2, x, 10 ** 9 + 7) - 2
    base %= 10 ** 9 + 7
print(base)
