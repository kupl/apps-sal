n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0, 0, 0, 0, 0]
d = [0, 0, 0, 0, 0]
for x in range(0, n):
    c[a[x] - 1] = c[a[x] - 1] + 1
    d[b[x] - 1] = d[b[x] - 1] + 1


def dingle():
    for x in range(0, 5):
        if (c[x] + d[x]) % 2 != 0:
            return -1
    f = 0
    for x in range(0, 5):
        f = f + abs((c[x] - d[x]) // 2)
    return f // 2


print(dingle())
