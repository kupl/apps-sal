n = int(input())
b = list(map(int, input().split()))

a = sorted(b)

a.sort()

max_i = 0
min_i = 0
maxv = -1 << 60
minv = 1 << 60
for i in range(n):
    if maxv < b[i]:
        maxv = b[i]
        max_i = i
    if minv > b[i]:
        minv = b[i]
        min_i = i

if (a[0] >= 0):
    print((n - 1))
    for i in range(n - 1):
        print((i + 1, i + 2))
elif (a[-1] <= 0):
    print((n - 1))
    for i in reversed(list(range(n - 1))):
        print((i + 2, i + 1))
elif (abs(a[0]) < abs(a[-1])):
    print((2 * n - 2))
    for i in range(n):
        if max_i == i:
            continue
        print((max_i + 1, i + 1))
    for i in range(n - 1):
        print((i + 1, i + 2))
else:
    print((2 * n - 2))
    for i in range(n):
        if min_i == i:
            continue
        print((min_i + 1, i + 1))
    for i in reversed(list(range(n - 1))):
        print((i + 2, i + 1))
