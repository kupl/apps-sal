import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# L と 2 ** n の差
L = ir()
length = L.bit_length()
edges = []
for i in range(1, length):
    edges.append((i, i+1, 0))
    edges.append((i, i+1, 2**(i-1)))

for i in range(length-1):
    if L >> i & 1:
        L -= 2**i
        edges.append((i+1, length, L))

print((length, len(edges)))
for e in edges:
    print((*e))

# 56

