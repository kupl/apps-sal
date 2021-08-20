(m, t, r) = [int(x) for x in input().strip().split()]
ghosts = [int(x) for x in input().strip().split()]
candles = [ghosts[0] - 1 - x + t for x in range(0, r)]
usedTimes = [ghosts[0] - 1 - x for x in range(0, r)]
res = r
for i in range(0, m):
    for j in range(0, r):
        candleTime = candles[j]
        if candleTime < ghosts[i]:
            possibleTime = ghosts[i] - 1
            canFindTime = False
            while possibleTime >= ghosts[i] - t:
                if usedTimes.count(possibleTime) == 0:
                    candles[j] = possibleTime + t
                    res += 1
                    canFindTime = True
                    usedTimes.append(possibleTime)
                    break
                else:
                    possibleTime -= 1
            if not canFindTime:
                res = -1
                break
    if res == -1:
        break
print(res)
