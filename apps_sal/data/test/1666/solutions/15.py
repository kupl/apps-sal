x, y, a, b = list(map(int, input().split()))

result = []
for i in range(a, x + 1):
    for j in range(b, min(i, y + 1)):
        result.append((i, j))
print(len(result))
for x, y in result:
    print(x, y)

