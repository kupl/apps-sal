(n, m) = map(int, input().split())
data = [input().split() for i in range(m)]
for i in range(1, n + 1):
    count = 0
    for j in range(m):
        if int(data[j][0]) == i or int(data[j][1]) == i:
            count += 1
    print(count)
