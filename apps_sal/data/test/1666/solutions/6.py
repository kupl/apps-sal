x, y, a, b = (int(x) for x in input().split())
val = []
for i in range(max(a, b + 1), x + 1):
    for j in range(b, min(i - 1, y) + 1):
        val.append((i, j))
print(len(val))
for o in val:
    print(o[0], o[1])
