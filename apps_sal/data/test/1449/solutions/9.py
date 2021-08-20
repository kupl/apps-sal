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
    (n, k) = list(map(int, input().split()))
    a = set(map(int, input().split()))
    n = len(a)
    if n == 1:
        ans = 1
    elif k == 1:
        ans = -1
    else:
        ans = ceil((n - 1) / (k - 1))
    print(ans)
'\nn,m=map(int,input().split())\ngraph=defaultdict(dict)\nfor i in range(m):\n    u,v,w=map(int,input().split())\n    graph[u][v]=w\n    graph[v][u]=w\ndef dij(u,v):\n    graph[u][v]*=2\n    graph[v][u]*=2\n    d={}\n    d[1]=0\n    for i in range(2,n+1):\n        d[i]=inf\n    remain=set(range(2,n+1))\n    for i in graph[1]:\n        d[i]=graph[1][i]\n    while remain:\n        k=min(remain,key=lambda x: d[x])\n        remain.remove(k)\n        for i in remain:\n            if i in graph[k]:\n                d[i]=min(d[i],d[k]+graph[k][i])\n    graph[u][v]//=2\n    graph[v][u]//=2\n    return d[n]\nD={}\nD[1]=0\nfor i in range(2,n+1):\n    D[i]=inf\nremain=set(range(2,n+1))\npre=[-1]*(n+1)\nfor i in graph[1]:\n    D[i]=graph[1][i]\n    pre[i]=1\nwhile remain:\n    k=min(remain,key=lambda x: D[x])\n    remain.remove(k)\n    for i in remain:\n        if i in graph[k]:\n            if D[i]>D[k]+graph[k][i]:\n                D[i]=D[k]+graph[k][i]\n                pre[i]=k\ncur=ans=D[n]\nnode=n\nwhile pre[node]!=-1:\n    ans=max(ans,dij(node,pre[node]))\n    node=pre[node]\nprint(ans-cur)\n            \n'
