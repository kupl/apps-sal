import sys
fin = sys.stdin

a = list(map(int, fin.readline().split()))

d = a[1] - a[0]

if a[2] - a[1] == a[3] - a[2] == d:
    print(a[3] + d)
else:
    d = a[1] / a[0]
    if a[2] / a[1] == a[3] / a[2] == d and d * a[3] == int(d * a[3]):
        print(int(d * a[3]))
    else:
        print(42)
