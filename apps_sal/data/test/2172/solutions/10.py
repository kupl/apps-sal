dictx = {}
a, b = list(map(int, input().split(' ')))

for i in range(b):
    x, y = list(map(str, input().split(' ')))
    if len(y) < len(x):
        dictx[x] = y
        dictx[y] = y
    else:
        dictx[y] = x
        dictx[x] = x

god = list(map(str, input().split(' ')))
strx = [dictx[i] for i in god]
print(' '.join(strx))
