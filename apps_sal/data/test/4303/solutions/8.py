N,K = map(int,input().split())
x = list(map(int,input().split()))
xp = [i for i in x if i >= 0]
xn = [i for i in x if i < 0]
xn.reverse()
lp = len(xp)
ln = len(xn)
if lp == 0:
    print(-xn[K-1])
    return
if ln == 0:
    print(xp[K-1])
    return
pc = min(K,lp)
pp = xp[pc-1]
if K>lp:
    nc = K-lp
    np = -xn[nc-1]
else:
    nc = 0
    np = 0
ans = pp + np + min(pp,np)
for i in range(pc-1):
    if nc == ln:
        break
    pp = xp[pc-i-2]
    np = -xn[nc]
    nc += 1
    ans = min(ans,pp + np + min(pp,np))
print(ans)
