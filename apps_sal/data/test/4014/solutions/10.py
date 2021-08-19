[n, m] = [int(x) for x in input().split()]
I = 0
S = 1
D = 2
C = 3
exses = [[0, 0, 0, 0]]
pops = [0] * (n + 1)
i = 1
while i <= m:
    [s, d, c] = [int(x) for x in input().split()]
    exses.append([i, s, d, c])
    pops[d] = i
    i += 1
i = 1
result = [0] * (n + 1)
fail = False
while i <= n:
    if pops[i] != 0 and exses[pops[i]][C] == 0:
        result[i] = m + 1
    elif pops[i] != 0 and exses[pops[i]][C] > 0:
        fail = True
        break
    else:
        ex = None
        min = n + 1
        for e in exses:
            if e[D] > i and e[S] <= i and (e[D] < min) and (e[C] > 0):
                min = e[D]
                ex = e
        if ex == None:
            result[i] = 0
        else:
            result[i] = ex[I]
            ex[C] -= 1
    i += 1
if fail:
    print(-1)
else:
    for x in result[1:]:
        print(x, end=' ')
