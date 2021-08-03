n = int(input())
res = []
used = [False] * n
used1 = [False] * n
for i in range(n * n):
    x, y = [int(x) for x in input().split()]
    if used[x - 1] == False and used1[y - 1] == False:
        res.append(i + 1)
        used[x - 1] = True
        used1[y - 1] = True
print(*res)
