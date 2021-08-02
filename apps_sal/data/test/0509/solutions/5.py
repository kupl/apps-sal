
n = int(input())
a = [int(input()) for x in range(0, n)]

for x in range(0, 2 ** n + 1):
    v = 0
    for p in range(0, n):
        if (x >> p) & 1 != 0:
            v += a[p]
        else:
            v -= a[p]

    if v % 360 == 0:
        print("YES")
        break
else:
    print("NO")
