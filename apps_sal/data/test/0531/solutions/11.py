n = int(input())
x = input().split()
x = [int(k) for k in x]
rem = []
x.sort()
mn = x[0]
mx = x[-1]
if mx - mn <= 1:
    print(len(x))
    for k in x:
        print(k, end=' ')
    print()
else:
    avg = mn + 1
    expsum = avg * len(x)
    sm = 0
    countmn = 0
    countavg = 0
    countmx = 0
    for k in x:
        sm += k
    if sm - expsum > 0:
        rem = x[len(x) - (sm - expsum):len(x)]
        x = x[0:len(x) - (sm - expsum)]
    if sm - expsum < 0:
        rem = x[0:expsum - sm]
        x = x[expsum - sm:len(x)]
    if len(x) % 2 == 1:
        rem.append(avg)
        for i in range(len(x)):
            if x[i] == avg:
                x = x[0:i] + x[i + 1:len(x)]
                break
    for k in x:
        if k == mn:
            countmn += 1
        if k == avg:
            countavg += 1
        if k == mx:
            countmx += 1
    if countmn + countmx < countavg:
        print(countmn + countmx + len(rem))
        for i in range(int(len(x) / 2)):
            rem.append(mn)
            rem.append(mx)
    else:
        print(countavg + len(rem))
        for i in range(len(x)):
            rem.append(avg)
    for k in rem:
        print(k, end=' ')
    print()
