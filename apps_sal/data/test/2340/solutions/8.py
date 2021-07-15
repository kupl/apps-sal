import sys
import math
input = sys.stdin.readline

q=int(input())
for i in range(q):
    h,n=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.append(0)
    count=0
    cur=0
    now=arr[cur]
    cur=1
    while cur<n:
       # print("now", now, "count", count)
        try:
            if now-arr[cur]==1:
                if now-arr[cur+1]==2:
                    now=arr[cur+1]
                    cur+=2
                else:
                    count+=1
                    now = arr[cur+1]+1
                    cur+=1
            else:
                now=arr[cur]+1
        except:
            break

    print(count)

