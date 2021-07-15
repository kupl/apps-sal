#! python3

def is_good(a, n, i, j):
    c = set([])
    for x in range(n):
        c.add(a[i][j] - a[i][x])
    for x in range(n):
        if a[x][j] in c:
            return True
    return False

n = int(input())
a = []
for _ in range(n):
    a.append([int(x) for x in input().strip().split(' ')])

good = True
for i in range(n):
    for j in range(n):
        if a[i][j] != 1 and not is_good(a, n, i, j):
            good = False
            break
if good:
    print("Yes")
else:
    print("No")

