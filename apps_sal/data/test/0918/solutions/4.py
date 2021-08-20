(n, m) = list(map(int, input().split()))
a = []
for i in range(m):
    a.append([])
for i in range(n):
    (s, c, b) = input().split()
    c = int(c)
    b = int(b)
    a[c - 1].append([-b, s])
for i in range(m):
    a[i].sort()
    if len(a[i]) == 2:
        print(a[i][0][1], a[i][1][1])
    else:
        aa = a[i][1][0]
        bb = a[i][2][0]
        if aa == bb:
            print('?')
        else:
            print(a[i][0][1], a[i][1][1])
