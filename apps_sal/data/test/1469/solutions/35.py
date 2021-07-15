import math


l = int(input())
node = int(math.log2(l)) + 1
edges = []

for _from in range(1, node):
    edges.append([_from, _from+1, 0])
    edges.append([_from, _from+1, 2**(_from-1)])

count = 2 ** (node-1)
lack = l - count
length = 2 ** (node-1)

for _from in range(node-1, 0, -1):
    if not lack:
        break
    add_line = 2 ** (_from-1)
    if add_line > lack:
        continue
    edges.append([_from, node, length])
    lack -= add_line
    length += add_line

print((node, len(edges)))
for _from, to, length in edges:
    print((_from, to, length))

