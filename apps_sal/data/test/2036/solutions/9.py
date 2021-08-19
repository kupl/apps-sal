n, m, x, y = list(map(int, input().split()))

print(x, y)
for i in range(1, m + 1):
    if i == y:
        continue
    print(x, i)

y_last = m
for i in range(1, n + 1):
    # print("> ---")
    if i == x:
        continue
    if y_last == m:
        for j in range(m, 0, -1):
            print(i, j)
        y_last = 1
        continue
    if y_last == 1:
        for j in range(1, m + 1):
            print(i, j)
        y_last = m
