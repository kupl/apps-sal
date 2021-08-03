import sys
import math
from collections import defaultdict
n, k = list(map(int, sys.stdin.readline().split()))
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
    '''if l[i]!=0:
        if k%l[i]!=0 and vis[l[i]]==0:
            vis[l[i]]=1
            x=math.gcd(k,l[i])
            st=0
            while st*x<k:
                ans.add(st*x)
                st+=1
            if x==1:
                print(len(ans))
                res=list(ans)
                res.sort()
                print(*res)
                return
        else:
            if vis[l[i]]==0:
                st=0
                vis[l[i]]=1
                while st*l[i]<k:
                    ans.add(st*l[i])
                    st+=1'''
st = 0
x = math.gcd(x, k)
while st * x < k and x != 0:
    ans.add(st * x)
    st += 1
print(len(ans))
res = list(ans)
res.sort()
print(*res)
