num = int(input())
ns = [*map(int, input().split())]
tri, edge = 0, 0
for n in ns:
    newTri = min(edge, n // 2)
    tri += newTri
    edge -= newTri
    n -= newTri * 2
    tri += n // 3
    n = n % 3
    edge += n
print(tri)
