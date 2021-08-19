def min(a, b):
    if a < b:
        return a
    else:
        return b


def max(a, b):
    if a > b:
        return a
    else:
        return b


n = int(input())
coor = [int(x) for x in input().split()]
mi = [0] * n
ma = [0] * n
for i in range(n):
    ma[i] = max(coor[n - 1] - coor[i], coor[i] - coor[0])
mi[0] = coor[1] - coor[0]
mi[n - 1] = coor[n - 1] - coor[n - 2]
for i in range(1, n - 1):
    mi[i] = min(coor[i] - coor[i - 1], coor[i + 1] - coor[i])
for i in range(n):
    print(mi[i], ma[i])
