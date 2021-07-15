import math
n, m, k = list(map(int,input().split()))
x, s = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
a.insert(0,x)
b.insert(0,0)
c.insert(0,0)
d.insert(0,0)
ans = 1<<100
for it in range(m+1):
    mana = s-b[it]
    if mana<0: continue
    lo, hi = 0, k
    while lo!=hi:
        mid = math.ceil((lo+hi)/2)
        if d[mid]<=mana: lo = mid
        else: hi = mid-1
    ans = min(ans,(n-c[lo])*a[it])
print(ans)

