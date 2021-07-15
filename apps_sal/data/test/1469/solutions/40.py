L = int(input())
N = L.bit_length()

node = [i for i in range(1, N + 1)]
edge = []

for x, y in zip(node[:-1], node[1:]):
    edge.append((x, y, 0))

x = 1
while L > 1:
    if L & 1:
        L -= 1
        edge.append((x, N, L))
    else:
        L //= 2
        edge.append((x, x + 1, L))
        x += 1

print(N, len(edge))
for e in edge:
    print(*e)
