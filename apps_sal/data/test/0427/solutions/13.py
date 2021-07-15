import math
def expr(N,x,y,cnt1,cnt2):
    cnt1 = max(cnt1res - math.floor(N/y)+math.floor(N/(y*x)),0)
    cnt2 = max(cnt2res - math.floor(N/x)+math.floor(N/(y*x)),0)
    b = N-math.floor(N/x)-math.floor(N/y)+math.floor(N/(x*y)) >= cnt1+cnt2
    return b
    
cnt1,cnt2,x,y = map(int,list(input().split()))
cnt1res = cnt1
cnt2res = cnt2
N = math.ceil((cnt1 + cnt2+1)/(1-1/x-1/y+1/(y*x)))

start,last = 1,N
while last>start:
    mid = start + (last-start)//2
    if expr(mid, x, y, cnt1, cnt2):
        last = mid
    else:
        start = mid
    if start+1==last:
        break
    
print(last)
