from bisect import *
from collections import *
from math import *
from heapq import *
from typing import List
from itertools import *
from operator import *
from functools import *
import sys
'\n@lru_cache(None)\ndef fact(x):\n    if x<2:\n        return 1\n    return fact(x-1)*x\n\n@lru_cache(None)\ndef per(i,j):\n    return fact(i)//fact(i-j)\n\n@lru_cache(None)\ndef com(i,j):\n    return per(i,j)//fact(j)\n\ndef linc(f,t,l,r):\n    while l<r:\n        mid=(l+r)//2\n        if t>f(mid):\n            l=mid+1\n        else:\n            r=mid\n    return l\n\ndef rinc(f,t,l,r):\n    while l<r:\n        mid=(l+r+1)//2\n        if t<f(mid):\n            r=mid-1\n        else:\n            l=mid\n    return l\n\ndef ldec(f,t,l,r):\n    while l<r:\n        mid=(l+r)//2\n        if t<f(mid):\n            l=mid+1\n        else:\n            r=mid\n    return l\n\ndef rdec(f,t,l,r):\n    while l<r:\n        mid=(l+r+1)//2\n        if t>f(mid):\n            r=mid-1\n        else:\n            l=mid\n    return l\n\ndef isprime(n):\n    for i in range(2,int(n**0.5)+1):\n        if n%i==0:\n            return False\n    return True\n\ndef power2(n):\n    while not n&1:\n        n>>=1\n    return n==1\n'
'\nimport time\ns=time.time()\ne=time.time()\nprint(e-s)\n'
t = int(input())
for i in range(t):
    (n, m) = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    used = set()
    ans = 0
    for i in range(n // 2 + 1):
        for j in range(m // 2 + 1):
            if (i, j) not in used:
                tmp = set([(i, j), (n - 1 - i, j), (n - 1 - i, m - 1 - j), (i, m - 1 - j)])
                used |= tmp
                if len(tmp) == 1:
                    continue
                elif len(tmp) == 2:
                    ((x, y), (a, b)) = tmp
                    ans += abs(arr[x][y] - arr[a][b])
                else:
                    res = []
                    for (x, y) in tmp:
                        res.append(arr[x][y])
                    res.sort()
                    ans += min((sum((abs(res[i] - res[j]) for j in range(4))) for i in range(1, 3)))
    print(ans)
'\nn,m=map(int,input().split())\na=[]\nb=[]\nc=[]\nd=[]\nfor i in range(n):\n    ai,bi=map(int,input().split())\n    a.append(ai)\n    b.append(bi)\nfor i in range(m):\n    ci,di=map(int,input().split())\n    c.append(ci)\n    d.append(di)\ndic={}\nfor i in range(n):\n    for j in range(m):\n        x=c[j]-a[i]+1\n        y=d[j]-b[i]+1\n        if x>0 and y>0:\n            if x in dic:\n                dic[x]=min(dic[x],y)\n            else:\n                dic[x]=y\n#print(dic)\nif not dic:\n    ans=0\nelse:\n    res=sorted(dic.items())    \n    n=len(res)\n    ans=res[-1][0]\n    ym=res[-1][1]\n    for i in range(n-2,-1,-1):\n        ans=min(ans,res[i][0]+ym)\n        ym=max(ym,res[i][1])\n    ans=min(ym,ans)\nprint(ans)\n'
