# -*- coding: utf-8 -*-
n, m = map(int, input().split(' '))
t = []
r = "NO"
for i in range(m):
    l = list(map(int, input().split(' ')))[1::]
    t.append(l)
for i in t:
    rik = []
    morti = []
    if r == "YES":
        break
    for j in i:
        if j < 0 and j not in rik:
            j = abs(j)
            rik.append(j)
            if j in morti:
                r = "NO"
                break
            else:
                r = "YES"
        elif j > 0 and j not in morti:
            morti.append(j)
            if j in rik:
                r = "NO"
                break
            else:
                r = "YES"
print(r)
