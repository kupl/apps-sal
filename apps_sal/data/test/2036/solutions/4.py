(n, m, x, y) = list(map(int, input().split()))
result = [(x, y)]
for j in range(1, m + 1):
    if j == y:
        continue
    result.append((x, j))
for i in range(1, n + 1):
    if i == x:
        continue
    last = result[-1][1]
    result.append((i, last))
    for j in range(1, m + 1):
        if j == last:
            continue
        result.append((i, j))
for t in result:
    print(t[0], t[1])
