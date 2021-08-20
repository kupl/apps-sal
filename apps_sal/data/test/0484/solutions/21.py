(n, A, B) = map(int, input().split())
l = []
for i in range(n):
    (x, y) = map(int, input().split())
    l.append((x, y))


def checkList(a, b):
    return a <= A and b <= B or (b <= A and a <= B)


def checkPear(ax, ay, bx, by):
    return checkList(ax + bx, max(ay, by)) or checkList(ax + by, max(ay, bx)) or checkList(ay + by, max(ax, bx)) or checkList(ay + bx, max(ax, by))


maxs = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if checkPear(*l[i], *l[j]):
            if l[i][0] * l[i][1] + l[j][0] * l[j][1] > maxs:
                maxs = l[i][0] * l[i][1] + l[j][0] * l[j][1]
print(maxs)
