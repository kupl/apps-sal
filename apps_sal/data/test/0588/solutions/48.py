n = int(input())
from cmath import phase
xy = sorted([list(map(int,input().split())) for i in range(n)],key=lambda x: phase(x[0]+x[1]*1j))
#x+yiのargument[-pi,pi]の小さい方から順に並べる
xy += xy
#同じものを複製
ans = 0
for l in range(n):
    a = [0,0] # 最後にたどり着く座標
    for r in range(l,min(2*n,l+n)):#l番目含めlからn個について
        a[0] += xy[r][0]
        a[1] += xy[r][1]
        ans = max(ans,abs(a[0]+a[1]*1j))
print(ans) 
