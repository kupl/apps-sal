a,b,c = map(int,input().split())
maxn = max(max(a,b),c)
minn = min(min(a,b),c)
midn = a + b + c - minn - maxn
ans = maxn - midn
anss = 1001001
if (maxn - ans - minn)%2 == 0:
  ans += (maxn - ans - minn)/2
else:
  ans += (maxn - ans - minn)//2 + 2
if (maxn - midn)%2 == (maxn - minn)%2:
  anss = (maxn - midn +1)//2 + (maxn - minn + 1)//2
ans = min(ans,anss)
print(int(ans))
