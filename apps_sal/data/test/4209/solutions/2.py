# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353 
INF = 100_000_000
# from heapq import heappush, heappop
from collections import defaultdict
t = 1#int(input())
# from math import sqrt


for test in range(t):
    n = int(input())
    # H, n = (map(int, input().split()))
    # a = []
    # for i in range(n):
    # l = input()
    # r = input()
    a = (list((list(map(int, input().split())))))
    pre = [0 for i in range(n+1)]

    for i in range(n):
        pre[i+1] = pre[i]+a[i]
    
    Sum = defaultdict(list)

    for i in range(n):
        for j in range(i, n):
            tmp = pre[j+1]-pre[i]
            # print(i,j,tmp)
            Sum[tmp].append((i,j))

    maxVal = 0
    maxSum = -1
    for key, val in list(Sum.items()):
        val.sort()
        tmp = 1
        cur = val[0][1]
        for i in range(1,len(val)):
            if val[i][0]>cur:
                tmp+=1
                cur = val[i][1]
            elif val[i][1]<=cur:
                cur = val[i][1]
        if maxVal < tmp:
            maxVal = tmp
            maxSum = key

    print(maxVal)
    val = Sum[maxSum]
    val.sort()
    ans = []
    ans.append(val[0])
    cur = val[0][1]
    for i in range(1,len(val)):
        if val[i][0]>cur:
            ans.append(val[i])
            cur = val[i][1]
        elif val[i][1]<=cur:
            ans.pop()
            ans.append(val[i])
            cur = val[i][1]
    for i in ans:
        print(i[0]+1, i[1]+1)




