n = int(input())
d = []
for i in range(n):
    x = input().split()
    d.append([int(x[0]) - 1, int(x[1]) - 1])
first = d[0][0]
second = d[0][1]
if (d[first][0] != second and d[first][1] != second):
    t = first;
    first = second
    second = t
ans = [1, first + 1]
nex = second
while (nex != 0):
    ans.append(nex + 1)
    if (d[first][0] == second):
        nex = d[first][1]
    else:
        nex = d[first][0]
    first = second
    second = nex
for i in ans:
    print(i, end=" ")
