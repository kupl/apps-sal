n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
from collections import deque
from collections import defaultdict
b = deque()
c = defaultdict(int)
for i in a:
    c[i]=0
l = 0
i = 0
while i<n:
    if l<k:
        if c[a[i]]==1:
            i=i+1
            continue
        else:
            b.appendleft(a[i])
            c[a[i]]=1
            l=l+1
            i=i+1
    else:
        if c[a[i]]==1:
            i=i+1
            continue
        else:
            e=b.pop()
            c[e]=0
            c[a[i]]=1
            b.appendleft(a[i])
            i=i+1
print(len(b))
print(*b)

