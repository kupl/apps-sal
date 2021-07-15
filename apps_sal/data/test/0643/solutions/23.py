def chec(a,b,p,q,mid):
    if p*r>=a and (q-p)*mid>=b-a:
        return True
    else:
        return False
def check(np, nq):
  return np >= a and nq >= b and (np - a <= nq - b)    
for _ in range(int(input())):
    a,b,p,q = list(map(int,input().split()))
    l=0
    r=10000000000
    if check(p*r,q*r)==False:
        print(-1)
        continue
    while l<=r:
        mid = l +(r-l)//2
        if check(p*mid,q*mid):
            r=mid-1
        else:
            l=mid+1
    print(l*q-b)

