n = int(input())
al = []
sl = set()
for i in range(n):
    al.append(list(input()))
for i in range(n - 2):
    for j in range(1, n - 1):
        if al[i][j] == al[i + 1][j] == al[i + 1][j - 1] == al[i + 1][j + 1] == al[i + 2][j] == "#":
            al[i][j] = al[i + 1][j] = al[i + 1][j - 1] = al[i + 1][j + 1] = al[i + 2][j] = "."
for i in range(n):
    sl = sl.union(set(al[i]))
if len(sl) == 1:
    print("YES")
else:
    print("NO")
