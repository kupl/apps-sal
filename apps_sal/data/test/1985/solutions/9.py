"""
from time import sleep
n,k=[int(i) for i in input().split()]

inf=[None for i in range(10**5)]
ans=[0 for i in range(10**5)]
def howMany(i):
    if i-k+1<0:
        inf[i]=1
        return
    elif i==k-1:
        inf[i]=2
        return 
    else:
        inf[i]=(inf[i-1]+inf[i-k])%(10**9+7)

for i in range(10**5):
    howMany(i)
    ans[i]=ans[i-1]+inf[i]
for i in range(n):
    a,b=[int(i)-1 for i in input().split()]
    print(ans[:20])
    print((a-1) if a-1>=0 else 0)
    print(ans[b]-ans[(a-1) if a-1>=0 else 0])%(10**9+7)

#a={'WWWRRRR','RWWWRRR','RRWWWRR','RRRWWWR','RRRRWWW','RRRRRRR','WWWWWWR','WWWRWWW','RWWWWWW'}
#print(len(a))
"""
k, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = []
ans = 0
test = set()
for i in a:
    c.append(i if c == [] else (c[-1] + i))


def howMany(a1):
    nonlocal ans
    # print(a1)
    for i in b:
        if not i in a1:
            return
    if a1[0] in test:
        return
    else:
        test.add(a1[0])
    # print(b[0]-a1[0])
    ans += 1


for i in c:
    howMany(list([b[0] - i + x for x in c]))
print(ans)
