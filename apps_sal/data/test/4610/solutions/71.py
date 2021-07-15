n,k = map(int,input().split())
a = list(map(int,input().split()))
import collections
c = collections.Counter(a)
li = []
ans = 0
for v,num in  c.items():
    li.append((v,num))
ll = sorted(li,key=lambda x: x[1],reverse=True)

for i in range(k,len(ll)):
    #print(ll[i][1])
    ans += ll[i][1]

print(ans)
