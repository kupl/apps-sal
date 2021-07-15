n, m = [int(x) for x in input().split()]

values = [1] * n
nodes = [list() for _ in range(n)]
spikes = [0] * n

for _ in range(m):
    n1, n2 = [int(x) for x in input().split()]
    if n1 > n2:
        n1, n2 = n2, n1
    nodes[n1-1].append(n2-1)
    spikes[n1-1] += 1
    spikes[n2-1] += 1

for i in range(0, n):
    for node in nodes[i]:
        values[node] = max(values[node], values[i] + 1)

m = max(list(range(n)), key=lambda i: spikes[i] * values[i])
print(spikes[m] * values[m])

