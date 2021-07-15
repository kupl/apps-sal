l,r,a = map(int,input().split())
l,r = min(l,r),max(l,r)
res = l
if a > r - l:
    res = r + (a - r + l) // 2
else:
    res += a
print(res * 2) 
