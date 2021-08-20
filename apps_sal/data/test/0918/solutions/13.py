(n, m) = map(int, input().split())
l = [[] for i in range(m)]
for i in range(n):
    a = input().split()
    (x, y) = (int(a[1]), int(a[2]))
    l[x - 1].append([y, a[0]])
for i in range(m):
    l[i].sort()
    if len(l[i]) > 2:
        if l[i][-2][0] == l[i][-3][0]:
            print('?')
        else:
            print(l[i][-1][1] + ' ' + l[i][-2][1])
    else:
        print(l[i][-1][1] + ' ' + l[i][-2][1])
