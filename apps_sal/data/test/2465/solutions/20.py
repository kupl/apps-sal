ans = [-1 for x in range(180 + 1)]
for i in range(3, 361):
    start = (i - 2) * 180 / i
    if start != int(start):
        continue
    # print(i, start)

    x = (180 - start) / 2

    for j in range(1, i - 1):
        if x * j == int(x * j) and ans[int(x * j)] == -1:
            ans[int(x * j)] = i
            # print(x * j, i)


n = int(input())

for _ in range(n):
    y = int(input())
    print(ans[y])

