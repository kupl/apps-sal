# JMD
# Nagendra Jha-4096


import sys
from math import ceil,floor

###Defines...###
mod = 1000000007


###FUF's...###
def nospace(l):
    ans = ''.join(str(i) for i in l)
    return ans


##### Main ####
t = 1
for tt in range(t):
    n=int(input())
    a=[]

    for i in range(n):
        a.append(float(input()))

    intcnt = 0

    for num in a:
        if(ceil(num)==floor(num)):
            intcnt+=1

    non_int = n-intcnt

    minsum=0
    ans=[]

    for num in a:
        minsum+=floor(num)
        ans.append(floor(num))

    if(abs(minsum)<=non_int ):
        cnt = abs(minsum)

        for i in range(n):
            if cnt == 0:
                break
            if(floor(a[i])!=ceil(a[i])):
                ans[i]+=1
                cnt-=1
        for num in ans:
            print(num)

    else:
        maxsum = 0
        newans = []

        for num in a:
            maxsum+=ceil(num)
            ans.append(ceil(num))

        assert(maxsum<=non_int)

        for i in range(n):
            if maxsum == 0:
                break
            if(floor(a[i])!=ceil(a[i])):
                ans[i]-=1
                maxsum-=1

        for num in ans:
            print(num)



