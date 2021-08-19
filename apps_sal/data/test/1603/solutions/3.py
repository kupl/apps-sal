from sys import stdin as cin
n = int(cin.readline())
a = list(list(map(int, cin.readline().split())))
b = sorted(a)
for i in range(1, n):
    a[i] += a[i - 1]
    b[i] += b[i - 1]
for i in range(int(cin.readline())):
    (q, x, y) = list(map(int, cin.readline().split()))
    if q == 1:
        if x == 1:
            print(a[y - 1] - a[x - 1] + a[0])
        else:
            print(a[y - 1] - a[x - 2])
    elif x == 1:
        print(b[y - 1] - b[x - 1] + b[0])
    else:
        print(b[y - 1] - b[x - 2])
