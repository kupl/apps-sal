n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
r = [a[i][0] - a[0][0] for i in range(n)]
c = [a[0][i] - a[0][0] for i in range(m)]
t = min(r)
r = [x - t for x in r]
t = min(c)
c = [x - t for x in c]
p = a[0][0] - r[0] - c[0]
if n < m:
    r = [x + p for x in r]
else:
    c = [x + p for x in c]
for i in range(n):
    for j in range(m):
        if r[i] + c[j] != a[i][j]:
            print(-1)
            quit()
print(sum(r) + sum(c))
for i, x in enumerate(r):
    for j in range(x):
        print("row", i + 1)
for i, x in enumerate(c):
    for j in range(x):
        print("col", i + 1)


# Made By Mostafa_Khaled
