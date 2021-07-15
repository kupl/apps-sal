L = int(input())
edges = []

p2 = 1
N = 1

""" 2べきのとき多重辺
   0     0     0     0  ...
1 === 2 === 3 === 4 === 5 ...
   1     2     4     8  ...
"""
while L >= p2 * 2:
    N += 1
    p2 *= 2
    edges.append((N - 1, N, 0))
    edges.append((N - 1, N, 2 ** (N - 2)))

rest = L - p2
tmp = p2
for i in range(N, -1, -1):
    if (rest >> i) & 1:
        edges.append((i + 1, N, tmp))
        tmp += 2 ** i

M = len(edges)
# assert N <= 20 and M <= 60
print((N, M))
for edge in edges:
    print((*edge))

