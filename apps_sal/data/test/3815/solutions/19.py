import math
def binpow(a,b,m):
    a %= m
    res = int(1)
    while b > 0 :
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res

def inv(a,m:int=1000000009):
    return binpow(a,m-2,m)

m=int(1000000009)

n,a,b,k=input().split()
n=int(n);a=int(a);b=int(b);k=int(k)
st=input()
res=int(1)
p=int((b*inv(a,m))%m)
itr=(n+1)//k
mul1=0
for i in range (len(st)):
    if st[i]=='+':
        mul1=(mul1+binpow(p,i,m))%m
    else:
        mul1=(mul1-binpow(p,i,m))%m
if binpow(p,k,m)==1:
    mul2=itr%m
else:
    mul2=((binpow(p,k*itr,m)-1)*inv((binpow(p,k,m)-1)%m))%m
res=(mul1*mul2)%m
left=n-k*itr+1
mul1=binpow(p,k*itr,m)
mul2=0
for i in range (left):
    if st[i]=='+':
        mul2=(mul2+binpow(p,i,m))%m
    else:
        mul2=(mul2-binpow(p,i,m))%m
res=(res+mul1*mul2)%m
res=(res*binpow(a,n,m))%m
print(res)



