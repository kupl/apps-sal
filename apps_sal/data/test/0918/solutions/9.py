class shkolnik():
    ball = 0

n, m = list(map(int, input().split()))

a = []


def ballsort(x):
    return x.ball


for i in range(m + 1):
    a.append([])

for i in range(n):
    c = shkolnik()
    c.family, reg, c.ball = input().split()
    c.ball = int(c.ball)
    a[int(reg)].append(c)

for i in range(1, m + 1):
    a[i].sort(key=ballsort)

for i in range(1, m + 1):
    if len(a[i]) > 2 and a[i][-2].ball == a[i][-3].ball:
        print("?")
    else:
        print(a[i][-1].family, a[i][-2].family)

