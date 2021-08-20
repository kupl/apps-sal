import math
(n, I) = [int(x) for x in input().split()]
lis = [int(x) for x in input().split()]
dic = dict()
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
disLis = sorted(dic)
nowK = len(disLis)
if math.log2(nowK) > I * 8 // n:
    maxK = 2 ** (I * 8 // n)
    needMin = nowK - maxK
    minChange = 0
    for i in range(needMin):
        minChange += dic[disLis[i]]
    befChange = minChange
    for i in range(1, needMin + 1):
        befChange = befChange - dic[disLis[needMin - i]] + dic[disLis[-i]]
        if befChange < minChange:
            minChange = befChange
    print(minChange)
else:
    print(0)
