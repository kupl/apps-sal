inflos = int(input())
parent = tuple(int(x) - 1 for x in input().split())

depth = [0]
for v in range(inflos - 1):
    depth.append(depth[parent[v]] + 1)

freq = {}

for d in depth:
    if d in freq:
        freq[d] += 1
    else:
        freq[d] = 1
res = 0
for d in freq:
    res += freq[d] % 2
print(res)
