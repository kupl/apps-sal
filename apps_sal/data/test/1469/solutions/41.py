L = int(input())

N = L.bit_length()

edges = [[] for _ in range(N)]
for i in range(N - 1):
    edges[i].append((i + 1, 0))
    edges[i].append((i + 1, 2**i))

now = 2**(N - 1)

for i in range(N - 1)[:: -1]:
    cnt = 2**i
    if L - now >= cnt:
        edges[i].append((N - 1, now))
        now += cnt

M = sum(len(edges[i]) for i in range(N))
print(N, M)

for i in range(N):
    for to, cost in edges[i]:
        print(i + 1, to + 1, cost)
