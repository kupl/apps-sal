import math
L = int(input())
N = math.floor(math.log2(L)) + 1
edge = []
for i in range(N - 1):
    edge.append((i + 1, i + 2, 0))
    edge.append((i + 1, i + 2, 1 << i))
for i in range(N - 1, 0, -1):
    if L - (1 << i - 1) >= 2 ** (N - 1):
        edge.append((i, N, L - (1 << i - 1)))
        L -= 1 << i - 1
print(N, len(edge))
for e in edge:
    print(str(e).lstrip('(').rstrip(')').replace(',', ''))
