(n, m, k) = map(int, input().split())
for i in range(n):
    a = [int(x) for x in input().split()]
d = []
for i in range(1, m):
    for j in range(i + 1, m + 1):
        if k == 0:
            d.append((i, j))
        else:
            d.append((j, i))
print(len(d))
for i in d:
    print(*i)
