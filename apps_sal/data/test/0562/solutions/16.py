n = int(input())
c = []
for i in range(n):
    a = list(map(int, input().strip().split(' ')))
    c.append(a)
c.sort()
if n <= 2:
    print('YES')
else:
    u = 0
    tv1 = []
    tv2 = []
    tv1.append(c[0])
    tv2.append(c[1])
    for i in range(2, n):
        if c[i][0] > tv1[0][1]:
            tv1[0] = c[i]
        elif c[i][0] > tv2[0][1]:
            tv2[0] = c[i]
        else:
            u = 1
            break
    if u == 0:
        print('YES')
    else:
        print('NO')
