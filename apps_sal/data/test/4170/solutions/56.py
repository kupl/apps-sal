import math
import collections
import itertools

def resolve():

    N=int(input())
    H=list(map(int,input().split()))

    Max=0
    cnt=0
    for i in range(1,N):
        if(H[i-1]>=H[i]):
            cnt+=1
        else:
            cnt=0
        Max=max(Max,cnt)

    print(Max)
    
resolve()

