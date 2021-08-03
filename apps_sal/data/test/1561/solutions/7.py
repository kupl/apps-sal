n, m, k = [int(x) for x in input().split()]
lst = []
v = 0
for i in range(n):
    s = list(input())
    lst.append(s)
for i in range(n):
    z = 0
    for j in range(m):
        if lst[i][j] == ".":
            z += 1
        else:
            z = 0
        if z >= k:
            v += 1
for i in range(m):
    z = 0
    for j in range(n):
        if lst[j][i] == ".":
            z += 1
        else:
            z = 0
        if z >= k:
            v += 1

if k == 1:
    v = v / 2
print(int(v))
