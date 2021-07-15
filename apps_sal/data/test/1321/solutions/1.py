ws = []
hs = []
a = int(input())

maxes = []
maxx = -1
for i in range(a):
    w, h = list(map(int, input().split(' ')))
    
    ws.append(w)
    hs.append(h)

hs2 = hs[:]
hs2.sort()
hs2.reverse()

fir = hs2[0]
sec = hs2[1]

t = sum(ws)
god = []
for i in range(a):
    if hs[i] == fir:
        god.append((t - ws[i]) * sec)
    else:
        god.append((t-ws[i])*fir)
print(' '.join([str(i) for i in god]))

