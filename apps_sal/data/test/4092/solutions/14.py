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
"\nfor i in range(t):\n    #n,m=map(int,input().split())\n    n,m=1,0\n    graph=defaultdict(set)\n    for i in range(m):\n        u,v=map(int,input().split())\n        graph[u-1].add(v-1)\n    visited=[0]*n\n    ans=[]\n    def delchild(u):\n        for child in graph[u]:\n            visited[child]=1\n            ans.append(child+1)\n    for i in range(n):\n        if not visited[i]:\n            children=graph[i]\n            if len(children)==1:\n                u=children.pop()\n                visited[u]=1\n                delchild(u)\n            elif len(children)==2:\n                u=children.pop()\n                v=children.pop()\n                if u in graph[v]:\n                    delchild(v)\n                    visited[v]=1\n                elif v in graph[u]:\n                    delchild(u)\n                    visited[u]=1\n                else:\n                    delchild(u)\n                    delchild(v)\n                    visited[u]=visited[v]=1\n    print(len(ans))\n    sys.stdout.flush()\n    print(' '.join(map(str,ans)))\n    sys.stdout.flush()\n\nimport time\ns=time.time()\ne=time.time()\nprint(e-s)\n"
'\nt=int(input())\nfor i in range(t):\n    #n,m=map(int,input().split())\n    n=int(input())\n    x=int(sqrt(n))\n    if x*x==n:\n        ans=2*x-2\n    elif x*(x+1)>=n:\n        ans=2*x-1\n    else:\n        ans=2*x\n    print(ans)\n'
n = int(input())
arr = list(map(int, input().split()))
d = {0}
pre = 0
ans = 0
for a in arr:
    pre += a
    if pre in d:
        ans += 1
        pre = a
        d = {0, a}
    else:
        d.add(pre)
print(ans)
