import math
import collections
import itertools

def resolve():

    N=int(input())
    B=list(map(int,input().split()))

    cnt=B[0]
    for i in range(N-2):
        if(B[i]<=B[i+1]):
            cnt+=B[i]
        else:
            cnt+=B[i+1]
    cnt+=B[N-2]
    print(cnt)
    
resolve()

