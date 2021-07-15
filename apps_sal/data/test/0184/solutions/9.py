l,r,a = list(map(int,input().split()))
if a > (max(l,r)-min(l,r)):
    print((l+a+r)//2*2)
else:
    print((min(l,r)+a) *2)

