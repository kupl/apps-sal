N,X,D = map(int,input().split())
if D==0:
    print(1 if X==0 else N+1)
    return
if D < 0:
    D *= -1
    X -= D*(N-1)

from collections import defaultdict
arrs = defaultdict(lambda: defaultdict(lambda: 0))
mni = mxi = 0
for k in range(N+1):
    d,m = divmod(k*X + D*mni, D)
    l = mxi - mni + 1
    arrs[m][d] += 1
    arrs[m][d+l] -= 1
    mni += k
    mxi += N-k-1

ans = 0
for arr in arrs.values():
    p = None
    c = 0
    for x,v in sorted(arr.items()):
        if c > 0:
            ans += x-p
        c += v
        p = x
print(ans)
