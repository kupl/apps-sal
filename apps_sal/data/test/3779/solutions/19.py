import sys
import math
from collections import defaultdict
(n, k) = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
l = [0 for _ in range(n)]
for i in range(n):
    l[i] = a[i] % k
ans = set()
ans.add(0)
vis = defaultdict(int)
x = 0
for i in range(n):
    x = math.gcd(x, l[i])
    'if l[i]!=0:\n        if k%l[i]!=0 and vis[l[i]]==0:\n            vis[l[i]]=1\n            x=math.gcd(k,l[i])\n            st=0\n            while st*x<k:\n                ans.add(st*x)\n                st+=1\n            if x==1:\n                print(len(ans))\n                res=list(ans)\n                res.sort()\n                print(*res)\n                return\n        else:\n            if vis[l[i]]==0:\n                st=0\n                vis[l[i]]=1\n                while st*l[i]<k:\n                    ans.add(st*l[i])\n                    st+=1'
st = 0
x = math.gcd(x, k)
while st * x < k and x != 0:
    ans.add(st * x)
    st += 1
print(len(ans))
res = list(ans)
res.sort()
print(*res)
