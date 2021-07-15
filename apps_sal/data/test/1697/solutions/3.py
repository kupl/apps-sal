n, m = map(int, input().split())
tabl = []
for l in range(n):
    tabl.append(list(input()))
def lstsos(i, j):
    nonlocal n, m
    ne = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for l, k in ne:
        if 0 <= l < n and 0 <= k < m:
            yield (l, k)
def degree(i, j):
    deg = 0
    for l, k in lstsos(i, j):
        deg += (tabl[l][k] == tabl[i][j])
    return deg
finished = False
while not finished:
    finished = True
    for l in range(n):
        for k in range(m):
            if tabl[l][k] != 'NO' and degree(l, k) in (0, 1):
                tabl[l][k] = 'NO'
                finished = False
cycle = False
for l in range(n):
    for k in range(m):
        if tabl[l][k] != 'NO':
            cycle = True
if cycle:
    print ("Yes")
else:
    print ("No")
