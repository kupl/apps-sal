import numpy as np
L = int(input())
branches = []
node_count = int(np.log2(L)) + 1
for n in range(node_count - 1):
    branches.append((n, n + 1, 0))
    branches.append((n, n + 1, 2 ** n))
byte_list = list(reversed(format(L, 'b')))[:-1]
a = 2 ** (node_count - 1)
for i in reversed(list(range(len(byte_list)))):
    if byte_list[i] == '1':
        branches.append((i, node_count - 1, a))
        a += 2 ** i
print((node_count, len(branches)))
for (u, v, w) in branches:
    print((u + 1, v + 1, w))
