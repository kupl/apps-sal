# Fast IO (only use in integer input)

# import os,io
# input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

t = int(input())
for _ in range(t):
    n = int(input())
    pointList = []
    pointOrderDict = {}
    interval = [] # (l,r) tuple
    intervalOrder = [] # interval list compressed as an order
    for _ in range(n):
        l,r = map(int,input().split())
        pointList.append(l)
        pointList.append(r)
        interval.append((l,r))
    pointList.sort()
    cnt = 0
    for i in range(2 * n):
        if i == 0 or pointList[i] != pointList[i-1]:
            pointOrderDict[pointList[i]] = cnt
            cnt += 1

    for elem in interval:
        intervalOrder.append((pointOrderDict[elem[0]],pointOrderDict[elem[1]]))
    
    intervalList = []
    dp = []

    for i in range(cnt):
        dp.append([])
        intervalList.append([])
        for j in range(cnt):
            dp[i].append(-1)

    for elem in intervalOrder:
        intervalList[elem[0]].append(elem[1])

    for i in range(cnt): # r - l
        for j in range(cnt - i): # l
            ans1 = 0 # is there [l,r]
            ans2 = 0 # max of [l+1,r] and [l,nr] + [nr + 1,r]
            if i != 0:
                ans2 = dp[j + 1][i + j]
            for elem in intervalList[j]:
                if elem == i + j:
                    ans1 += 1
                elif elem < i + j and ans2 < dp[j][elem] + dp[elem + 1][i + j]:
                    ans2 = dp[j][elem] + dp[elem + 1][i + j]
            dp[j][i+j] = ans1 + ans2
    
    print(dp[0][cnt - 1])
