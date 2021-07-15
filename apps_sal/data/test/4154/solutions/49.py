n,m = map(int,input().split())
lmax, rmin = 0, n

for _ in range(m):
  l,r = map(int,input().split())
  lmax = max(lmax, l)
  rmin = min(rmin, r)

print((rmin-lmax)+1 if (rmin-lmax)+1 > 0 else 0)
