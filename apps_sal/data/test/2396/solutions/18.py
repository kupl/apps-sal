# codeforces.com/contest/958/problem/D1

m = int(input())
positions = []
poscount = {}
for i in range(m):
    crew = list(input())
    n = len(crew)
    i = 1
    a = ''
    while crew[i] != '+':
        a += crew[i]
        i += 1
    b = ''
    i += 1
    while crew[i] != ')':
        b += crew[i]
        i += 1
    c = ''
    i += 2
    while i < n:
        c += crew[i]
        i += 1
    a = int(a)
    b = int(b)
    c = int(c)
    res = (a + b) / c
    positions.append(res)
    if res in poscount:
        poscount[res] += 1
    else:
        poscount[res] = 1

ans = []
for i in range(m):
    ans.append(poscount[positions[i]])
print(*ans, sep=' ')
