import math
n, m = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(input().strip())
digit = 0
alpha = 0
spec = ['&', '
dis = []
for i in range(n):
    s = l[i]
    j = 0
    mindigit = m
    minalpha = m
    minsp = m
    maxdigit = 0
    maxalpha = 0
    maxsp = 0
    while(j < m):
        if(s[j] in spec):
            if(minsp > j):
                minsp = j
            if(maxsp <= j):
                maxsp = j + 1
        elif(ord(s[j]) >= 48 and ord(s[j]) < 58):
            if(mindigit > j):
                mindigit = j
            if(maxdigit <= j):
                maxdigit = j + 1
        elif(ord(s[j]) >= 97 and ord(s[j]) < 123):
            if(minalpha > j):
                minalpha = j
            if(maxalpha <= j):
                maxalpha = j + 1
        j += 1
    dis.append([min(mindigit, m + 1 - maxdigit), min(minalpha, m + 1 - maxalpha), min(minsp, m + 1 - maxsp)])
mindis = 1000
for i in range(n):
    for j in range(n):
        for k in range(n):
            if(i != j and j != k and k != i):
                if(dis[i][0] != m and dis[j][1] != m and dis[k][2] != m):
                    if(mindis > dis[i][0] + dis[j][1] + dis[k][2]):
                        mindis = dis[i][0] + dis[j][1] + dis[k][2]
print(mindis)
