import io
import os
import sys
import math
import heapq


input = sys.stdin.readline
mod = 10**9 + 7
 
t = int(input())


for _ in range(t):
    x,y = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = arr + arr + arr
    
    for z in range(20):
        for i in range(1,16):
            arr[i] = min(arr[i], arr[i-1] + arr[i+1])
            
    c1,c2,c3,c4,c5,c6 = (arr[6:12])
    if x>=0 and y>=0:
        ans = 0
        mm = min(x,y)
        x -= mm
        y -= mm
        ans += mm * c1
        ans += y*c2
        ans += x*c6
        print(ans)
    elif x>=0 and y<0:
        ans = 0
        ans += abs(y)*c5
        ans += x*c6
        print(ans)
    elif x<0 and y<0:
        ans = 0
        x,y = abs(x),abs(y)
        mm = min(x,y)
        x -= mm
        y -= mm
        ans += mm * c4
        ans += y*c5
        ans += x*c3
        print(ans)
    else:
        ans = 0
        ans += abs(y) * c2
        ans += abs(x) * c3
        print(ans)
