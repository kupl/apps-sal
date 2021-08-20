def dista(a, b):
    return abs(lista[a][0] - lista[b][0]) + abs(lista[a][1] - lista[b][1])


lista = []
ne = 0
n = int(input())
dist = [0] * (n + 1)
lista.append((0, 0))
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    lista.append((x, y))
lista = sorted(lista, key=lambda x: min(x))
lista = sorted(lista, key=lambda x: max(x))
n += 1
ini = 0
ne = 1
oy = 0
ox = 0
while ne < n:
    ini = ne
    maxi = max(lista[ne])
    while ne < n and max(lista[ne]) == maxi:
        ne += 1
    minx = ini
    miny = ini
    for i in range(ini, ne):
        if lista[i][0] < lista[minx][0]:
            minx = i
        elif lista[i][0] == lista[minx][0] and lista[i][1] > lista[minx][1]:
            minx = i
        if lista[i][1] < lista[miny][1]:
            miny = i
        elif lista[i][1] == lista[miny][1] and lista[i][0] > lista[miny][0]:
            miny = i
    mxy = dista(minx, miny)
    if dista(miny, ox) + dist[ox] < dist[oy] + dista(miny, oy):
        dist[minx] = dista(ox, miny) + dist[ox] + mxy
    else:
        dist[minx] = dista(oy, miny) + dist[oy] + mxy
    if dista(ox, minx) + dist[ox] < dist[oy] + dista(oy, minx):
        dist[miny] = dista(ox, minx) + dist[ox] + mxy
    else:
        dist[miny] = dista(oy, minx) + dist[oy] + mxy
    ox = minx
    oy = miny
print(min(dist[miny], dist[minx]))
