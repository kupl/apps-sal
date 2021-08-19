l = []
for i in range(8):
    (x, y) = list(map(int, input().split()))
    l.append((x, y))
l.sort()
lx = []
lx.append(l[0][0])
lx.append(l[3][0])
lx.append(l[5][0])
ly = []
ly.append(l[0][1])
ly.append(l[1][1])
ly.append(l[2][1])
eps = [(x, y) for x in lx for y in ly]
eps.pop(4)
if l == eps and lx[0] != lx[1] and (lx[0] != lx[2]) and (lx[1] != lx[2]) and (ly[0] != ly[1]) and (ly[0] != ly[2]) and (ly[1] != ly[2]):
    print('respectable')
else:
    print('ugly')
