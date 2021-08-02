import sys
import math
n = int(input())
arr = list(map(int, sys.stdin.readline().split(' ')))
l = [0 for i in range(n)]
l[0] = -1
if(n == 1):
    print(arr[0])

else:
    if(arr[0] > arr[1]):
        m1 = arr[0]
        index = 0
        m2 = arr[1]
        l[0] += 1

    elif(arr[0] < arr[1]):
        index = 1
        m1 = arr[1]
        m2 = arr[0]
        l[1] -= 1

    for i in range(2, n):
        if(arr[i] <= m1):
            if(arr[i] > m2):
                l[index] += 1
                m2 = arr[i]
        else:
            l[i] -= 1
            m2 = m1
            m1 = arr[i]
            index = i
    mm = -10**9
    ans = 10**18

    for i in range(n):
        if(l[i] > mm):
            mm = l[i]
            ans = arr[i]
        elif(l[i] == mm):
            ans = min(arr[i], ans)
    print(ans)
