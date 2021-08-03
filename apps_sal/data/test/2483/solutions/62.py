n, c = map(int, input().split())
chan = [[] for _ in range(c)]
for _ in range(n):
    s, t, sc = map(int, input().split())
    sc -= 1
    chan[sc].append((s, t))
for i in range(c):
    chan[i].sort()
# print(chan)
for i in range(c):
    lis = []
    if len(chan[i]) == 1:
        lis.append(chan[i][0][0])
        lis.append(chan[i][0][1])
    elif len(chan[i]) >= 2:
        lis.append(chan[i][0][0])
        for j in range(len(chan[i]) - 1):
            if chan[i][j][1] != chan[i][j + 1][0]:
                lis.append(chan[i][j][1])
                lis.append(chan[i][j + 1][0])
        lis.append(chan[i][j + 1][1])
    chan[i] = lis
# print(chan)
accum = [0] * (10**5 + 2)
for i in range(c):
    for j in range(0, len(chan[i]) - 1, 2):
        accum[chan[i][j]] += 1
        accum[chan[i][j + 1] + 1] -= 1
for i in range(10**5 + 1):
    accum[i + 1] += accum[i]
# print(accum)
print(max(accum))
