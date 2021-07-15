n , k = list(map(int, input().split()))
v = list(map(int,input().split()))
ma = float('INF')*(-1)
m = min(n,k)
for i in range(m+1):
    for j in range(m+1-i):
        vl=v[:i]
        vr=v[n-j:]
        ans = sum(vl)+sum(vr)
        vb=vl+vr
        vb.sort()
        m2 = min(k-i-j, len(vb))
        for l in range(m2):
            if vb[l]<0:
                ans-=vb[l]
            else:
                break
        ma = max(ans,ma)
if ma<0:
    ma = 0
print(ma)

