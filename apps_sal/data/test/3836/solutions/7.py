n = int(input())
a = [[] for i in range(4)]

for i in range(n):
    s, influence = [i for i in input().split()]
    a[int(s, 2)].append(int(influence))

for i in range(4):
    a[i].sort(reverse=True)


def check():
    x = len(a[1])
    y = len(a[2])
    xy = len(a[3])
    z = len(a[0])

    if(xy + y == 0 or xy + x == 0):
        print(0)
        return

    w = min(x, y)
    sum0 = 0
    sum0 += sum(a[1][:w]) + sum(a[2][:w]) + sum(a[3])
    choose = 2
    if x >= y:
        choose = 1
    num = 0
    i = w
    j = 0
    while(i < max(x, y) and j < z and num < xy):
        if(a[choose][i] >= a[0][j]):
            sum0 += a[choose][i]
            i += 1
        else:
            sum0 += a[0][j]
            j += 1
        num += 1

    while(i < max(x, y) and num < xy):
        sum0 += a[choose][i]
        i += 1
        num += 1

    while (j < z and num < xy):
        sum0 += a[0][j]
        j += 1
        num += 1
    print(sum0)


check()
