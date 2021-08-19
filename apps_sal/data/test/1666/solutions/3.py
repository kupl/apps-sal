(x, y, a, b) = list(map(int, input().split()))
Results = []
for i in range(a, x + 1):
    for j in range(b, y + 1):
        if j >= i:
            continue
        Results.append((i, j))
print(len(Results))
Results.sort()
for item in Results:
    print(item[0], item[1])
