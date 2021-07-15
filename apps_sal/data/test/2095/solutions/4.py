n = int(input())

a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

res = []
for i in range(n):
    ok = True
    for j in range(n):
        if a[i][j] == 1 or a[i][j] == 3:
            ok = False
    if ok:
        res.append(i + 1)

print(len(res))
print(" ".join((str(x) for x in res)))
