n = int(input())
a = list(map(int, input().split()))
g = {}
for q in a:
    g[q] = g.get(q, 0) + 1
max_quantity = max(g, key=lambda x: g[x])
print(len(a) - g[max_quantity])
index_max = a.index(max_quantity)
for q in range(index_max - 1, -1, -1):
    if a[q] > max_quantity:
        print(2, q + 1, q + 2)
    else:
        print(1, q + 1, q + 2)
for q in range(index_max + 1, len(a)):
    if a[q] > max_quantity:
        print(2, q + 1, q)
    elif a[q] < max_quantity:
        print(1, q + 1, q)
