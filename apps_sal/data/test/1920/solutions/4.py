n = int(input())
p = []
for i in range(n):
    s, t, j = input().split()
    t = int(t)
    j = int(j)
    p.append([t, 'a', s])
    p.append([j, 'z', s])
p.sort()
e1 = 0
e2 = 0
maxi = 0
for i in range(2 * n):
    if p[i][1] == 'a' and p[i][2] == 'M':
        e1 += 1
    elif p[i][1] == 'a' and p[i][2] == 'F':
        e2 += 1
    elif p[i][1] == 'z' and p[i][2] == 'M':
        e1 -= 1
    else:
        e2 -= 1
    maxi = max(maxi, min(e1, e2))
print(maxi * 2)
        

