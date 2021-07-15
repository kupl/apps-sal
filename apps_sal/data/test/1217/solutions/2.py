a, b = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
a.sort()
bp = [[b[i], i, 0] for i in range(len(b))]
bp.sort()
a.append(10**15)
ptr = 0
cum = 0
ind = 0;
while ptr < len(a) and ind < len(bp):
    while (bp[ind][0] >= a[ptr]):
        ptr+=1
    bp[ind][2] = ptr
    ind += 1
bp.sort(key = lambda x:x[1])
for i in bp:
    print(i[2], end = ' ')

