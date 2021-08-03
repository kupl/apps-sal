import sys
import math as mt
# input=sys.stdin.buffer.readline
# t=int(input())
t = 1
for __ in range(t):
    n, k = list(map(int, input().split()))
    arr = []
    lr = {}
    d = {}
    ans = 0
    for i in range(n):
        arr.append(input())
        lr[i] = []
        for j in range(n):
            if arr[i][j] == 'B':
                lr[i].append(j)
                break
        for j in range(n - 1, -1, -1):
            if arr[i][j] == 'B':
                lr[i].append(j)
                break
        if len(lr[i]) == 0:
            lr[i].append(-1)
            lr[i].append(-1)
            d[i] = 1
            ans += 1
        else:
            d[i] = 0
    lr1 = {}
    d1 = {}
    for j in range(n):
        lr1[j] = []
        for i in range(n):
            if arr[i][j] == 'B':
                lr1[j].append(i)
                break
        for i in range(n - 1, -1, -1):
            if arr[i][j] == 'B':
                lr1[j].append(i)
                break
        if len(lr1[j]) == 0:
            d1[j] = 1
            ans += 1
            lr1[j].append(-1)
            lr1[j].append(-1)

        else:
            d1[j] = 0
    # print(arr,lr)
    a = {}

    i1 = 0
    fans1 = [[0 for j in range(n)] for i in range(n)]
    fans2 = [[0 for j in range(n)] for i in range(n)]
    for i1 in range(n - k + 1):
        a[i1] = []
        ans1 = 0
        # print(33,i1,i1+k-1)
        for i in range(k):
            if d[i] == 0:
                if k + i1 > lr[i][1] and i1 <= lr[i][0]:
                    ans1 += 1
        # print(111,ans1)

        # a[i1].append(ans1)
        fans1[0][i1] = ans1
        for i in range(n - k):
            if d[i] == 0 and k + i1 > lr[i][1] and i1 <= lr[i][0]:
                ans1 -= 1
            if d[i + k] == 0 and lr[i + k][1] < k + i1 and i1 <= lr[i + k][0]:
                ans1 += 1
            fans1[i + 1][i1] = ans1
            # a[i1].append(ans1)
    b = {}
    # print(arr,lr1,d1)
    for i1 in range(n - k + 1):
        b[i1] = []
        ans1 = 0
        # print(33,i1,i1+k-1)
        for i in range(k):
            if d1[i] == 0:
                if k + i1 > lr1[i][1] and i1 <= lr1[i][0]:
                    ans1 += 1
        # print(111,ans1)
        fans2[i1][0] = ans1
        b[i1].append(ans1)
        for i in range(n - k):
            if d1[i] == 0 and k + i1 > lr1[i][1] and i1 <= lr1[i][0]:
                ans1 -= 1
            if d1[i + k] == 0 and lr1[i + k][1] < k + i1 and i1 <= lr1[i + k][0]:
                ans1 += 1
            fans2[i1][i + 1] = ans1
            b[i1].append(ans1)

        # print(fans)
    maxi = 0
    for i in range(n):
        for j in range(n):
            maxi = max(fans1[i][j] + fans2[i][j], maxi)

    # print(fans1)
    # print(fans2)
    print(maxi + ans)
    # n=int(input())
    # h=list(map(int,input().split()))
