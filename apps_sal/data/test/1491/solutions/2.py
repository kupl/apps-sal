n = int(input())
arr = list(map(int, input().strip().split(' ')))
sq = 0
nsq = 0
sqq = []
nsqq = []
for i in arr:
    t = int(i**.5)
    if(t * t == i):
        sq += 1
        sqq.append(i)
    else:
        nsq += 1
        nsqq.append(i)
if(sq == nsq):
    print(0)
elif(sq > nsq):
    d = sq - n // 2
    cost = []
    for i in sqq:
        if(i != 0):
            cost.append(1)
        else:
            cost.append(2)
    cost.sort()
    s = 0
    for i in range(d):
        s += cost[i]
    print(s)
else:
    d = nsq - n // 2
    cost = []
    for i in nsqq:
        t = int(i**.5)
        pp = t * t
        ppp = (t + 1) * (t + 1)
        cost.append(min(abs(i - pp), abs(i - ppp)))
    cost.sort()
    s = 0
    for i in range(d):
        s += cost[i]
    print(s)
