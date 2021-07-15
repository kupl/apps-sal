A,B=list(map(int,input().split()))

def solve(A):
    ret=0
    res=1
    if A%4==1 or A%4==2:
        ret+=res
    dig=A%2
    res<<=1
    A>>=1
    while A>0:
        if dig==0 and A%2==1:
            ret+=res
        res<<=1
        A>>=1
    return ret

print((solve(B)^solve(A-1)))

