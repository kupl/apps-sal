n,i0,i1 = list(map(int, input().split()))
i0-=1

def len(n):
    l=1
    if n>1: l+=2*len(n//2)
    return l

def get(n, i):
    l=len(n)
    m=l//2
    a=0
    if m<=i:
        a+=n//2
        if m<i: a+=n%2
        i-=m+1
    if 0<i:a+=get(n//2,i)
    return a
    
a=get(n,i1)-get(n,i0)
print(a)

