n, m = input().split()
n = int(n)
m = int(m)
nList = input().split()
bList = [0] * len(nList)
for i in range(len(nList)):
    nList[i] = int(nList[i])
shopD = {}
shopT = {}
oHis = []
mHis = []
maxD = 0
for i in range(m):
    d, t = input().split()
    if nList[int(t) - 1] != 0:
        maxD = max(maxD, int(d))
        if d not in list(shopD.keys()):
            shopD.update({d: [int(t)]})
        else:
            if int(t) not in shopD[d]:
                shopD[d].append(int(t))
        if t not in list(shopT.keys()):
            shopT.update({t: [int(d)]})
        else:
            if int(d) not in shopT[t]:
                shopT[t].append(int(d))
for i, j in list(shopT.items()):
    j = list(dict.fromkeys(j))
    j.sort()
    shopT[i] = j
for i, j in list(shopD.items()):
    j = list(dict.fromkeys(j))
    shopD[i] = j
total = sum(nList)
coin = 0
day = 0
def modifyMis(t, left):
    if left == 0:
        for ii in range(len(mHis))[::-1]:
            if mHis[ii]['t'] == t:
                mHis.pop(ii)
    else:
        for ii in range(len(mHis))[::-1]:
            if mHis[ii]['t'] == t:
                mHis[ii]['n'] = left
while total > 0 and day < maxD:
    coin += 1
    day += 1
    oHis.append({'t': [], 'n': []})
    if str(day) in list(shopD.keys()):
        for t in shopD[str(day)]:
            if nList[t - 1] > 0:
                if bList[t - 1] > 0 and shopT[str(t)][0] != day and coin > nList[t - 1] - bList[t - 1] and len(mHis) > 0 and coin > 0:
                    i = 0
                    j = 0
                    while shopT[str(t)][i] < day:
                        extraC = 0
                        d = shopT[str(t)][i]
                        if t in oHis[d - 1]['t']:
                            indexT = oHis[d - 1]['t'].index(t)
                            extraC += oHis[d - 1]['n'][indexT]
                            bList[t - 1] -= oHis[d - 1]['n'][indexT]
                            total += oHis[d - 1]['n'][indexT]
                            oHis[d - 1]['t'].pop(indexT)
                            oHis[d - 1]['n'].pop(indexT)
                        while j < len(mHis) and mHis[j]['d'] < d:
                            j += 1
                        while extraC > 0 and len(mHis) > j:
                            thisT = mHis[j]['t']
                            thisD = mHis[j]['d']
                            change = min(extraC, mHis[j]['n'])
                            bList[thisT - 1] += change
                            total -= change
                            extraC -= change
                            mHis[j]['n'] -= change
                            modifyMis(thisT, nList[thisT - 1] - bList[thisT - 1])
                            if thisT in oHis[thisD - 1]['t']:
                                oHis[thisD - 1]['n'][oHis[thisD - 1]['t'].index(thisT)] += change
                            else:
                                oHis[thisD - 1]['t'].append(thisT)
                                oHis[thisD - 1]['n'].append(change)
                        i += 1
                        coin += extraC
            buy = min(nList[t - 1] - bList[t - 1], coin)
            if buy != 0:
                oHis[day - 1]['t'].append(t)
                oHis[day - 1]['n'].append(buy)
                total -= buy
                bList[t - 1] += buy
                modifyMis(t, nList[t - 1] - bList[t - 1])  
                coin -= buy
            if nList[t - 1] - bList[t - 1] > 0:
                mHis.append({'d': day, 't': t, 'n': nList[t - 1] - bList[t - 1]}) 
    if coin >= total * 2:
        break
day += max(total * 2 - coin, 0)
print(day)

