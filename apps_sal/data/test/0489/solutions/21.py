n = int(input())
a = sorted(map(int, input().split()))
x, y, z = a[0], a[1], a[2]
if x < y < z:
    print(a.count(z))
elif x < y <= z:
    c = a.count(y)
    print(c * (c - 1) // 2)
elif x <= y < z:
    print(a.count(z))
else:
    c = a.count(z)
    print(c * (c - 1) * (c - 2) // 6)
