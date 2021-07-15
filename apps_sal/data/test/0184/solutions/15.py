l,r,a=list(map(int, input().split()))
l, r = min(l,r), max(l,r)
b = r-l
if b<=a:
    a-=b
    print((r+a//2)*2)
else:
    print((l+a)*2)
    

