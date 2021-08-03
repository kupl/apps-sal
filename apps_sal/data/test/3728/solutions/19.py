n, m = map(int, input().split(' '))
a = []
for i in range(n):
    a.append(list(map(int, input().split(' '))))

p = []
possible = True
col_swap = False
# print('swaps:')
for r in a:
    x = []
    j = 0
    swaps = []
    while j < len(r) and len(swaps) < 3:
        if r[j] != j + 1:
            tmp = r[j]
            r[j] = r[tmp - 1]
            r[tmp - 1] = tmp
            swaps.append((j, tmp - 1))
        else:
            j += 1
    # print(swaps)
    if len(swaps) > 2:
        possible = False
        break
    if len(swaps) == 2:
        col_swap = True
    if len(swaps) > 0:
        x = swaps
        if len(swaps) == 2 and swaps[0][0] == swaps[1][0]:
            x.append((
                min(swaps[0][1], swaps[1][1]),
                max(swaps[0][1], swaps[1][1])
            ))
        p.append(x)

#print('possible:', possible, 'p:', p, 'col_swap:', col_swap)
if possible and col_swap and p:
    c = set(p[0])
    for x in p:
        c = c.intersection(x)
    possible = bool(c)
    #print('c:', c)

if possible:
    print('YES')
else:
    print('NO')
