n = int(input())
b = list(map(int,input().split()))
bmin = min(b)
bmax = max(b)
if bmin != bmax:
    print(bmax-bmin, b.count(bmin)*b.count(bmax)) 
else:
    print(0, n*(n-1)//2)
