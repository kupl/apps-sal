n = int(input())
res = 'YES'
uch = {}
zap = [0, 0]
for i in range(0, n):
    zap = list(map(int, input().split()))
    if zap[1] in uch:
        if zap[0] == uch[zap[1]] + 1:
            uch[zap[1]] = zap[0]
        else:
            if zap[0] > uch[zap[1]] + 1:
                res = 'NO'
    else:
        if zap[0] == 0:
            uch[zap[1]] = zap[0]
        else:
            res = 'NO'
print(res)
