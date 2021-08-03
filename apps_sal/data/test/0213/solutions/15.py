k = []
n, m = list(map(int, input().split(" ")))
for i in range(m):
    x, y = list(map(int, input().split(' ')))
    k.append([x, y])


def ok(x):
    for i in k:
        if (i[0] - 1) // x + 1 != i[1]:
            return False
    return True


poss = []
for x in range(1, 101):
    if ok(x):
        poss.append((n - 1) // x + 1)

if len(list(set(poss))) == 1:
    print(poss[0])
else:
    print(-1)
