def ii(): return int(input())
def si(): return input()
def mi(): return map(int,input().split())
def li(): return list(mi()) 

import math


for i in range(ii()):
    h,m=mi()
    ans=1440-(h*60+m)
    print(ans)
