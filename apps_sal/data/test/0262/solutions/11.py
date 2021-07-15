#B
n = int(input())
a = [list(map(int,input().split())) for j in range(n)]

if n == 1:
    print(1)
    return

for j in range(n):
    for i in range(n):
        if a[j][i] == 0:
            y = j
            x = i
            break

slist = []
for j in range(n):
    if j == y:
        continue
    ss = 0
    for i in range(n):
        ss += a[j][i]
    slist.append(ss)

for i in range(n):
    if i == x:
        continue
    ss = 0
    for j in range(n):
        ss += a[j][i]
    slist.append(ss)

if x != y:
    ss = 0
    for i in range(n):
        ss += a[i][i]
    slist.append(ss)

if x != n - 1 - y:
    ss = 0
    for i in range(n):
        ss += a[n - 1 - i][i]
    slist.append(ss)

slist.sort()

if slist[0] != slist[-1]:
    print(-1)
    return

s = slist[0]
s1 = s
s2 = s
s3 = s
s4 = s

for i in range(n):
    s1 -= a[y][i]

for i in range(n):
    s2 -= a[i][x]

if x == y:
    for i in range(n):
        s3 -= a[i][i]
else:
    s3 = s1

if x == n - 1 - y:
    for i in range(n):
        s4 -= a[n - 1 - i][i]
else:
    s4 = s1

if s1 == s2 == s3 == s4 and s1 > 0:
    print(s1)
else:
    print(-1)
