(n, k) = list(map(int, input().split()))
ks = k
l = []
for i in range(n):
    p = []
    for j in range(n):
        p.append(0)
    l.append(p)
if k > n ** 2:
    print(-1)
else:
    for i in range(n):
        for j in range(n):
            if k == 0:
                break
            if i == j:
                k -= 1
                l[i][j] = 1
            elif k > 1 and l[j][i] == 0:
                k -= 2
                l[i][j] = 1
                l[j][i] = 1
    ones = 0
    for row in l:
        ones += row.count(1)
    if ones != ks:
        print(-1)
    else:
        for i in l:
            s = ''
            for j in i:
                s += ' ' + str(j)
            print(s[1:])
