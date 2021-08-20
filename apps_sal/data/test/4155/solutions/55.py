n = int(input())
h = list(map(int, input().split(' ')))
cnt = 0
minNum = 0
tmp = 0
while True:
    for i in range(h.count(0)):
        if h.index(0) == 0:
            h.pop(0)
        elif h.index(0) > 0:
            tmp = h.index(0)
            break
    else:
        tmp = len(h)
    if not h:
        break
    if tmp == 1:
        cnt += h[0]
        h.pop(0)
    else:
        minNum = min(h[0:tmp])
        cnt += minNum
        for j in range(tmp):
            h[j] -= minNum
print(cnt)
