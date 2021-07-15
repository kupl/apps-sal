
s=input()
k=int(input())
N=len(s)
m=1000000007

a=m+1-pow(2,N*k,m)
b=m+1-pow(2,N,m)
l=(a*pow(b,m-2,m))%m

p=0
for i in range(N):
    if s[i] in ('0','5'):
        p=(p+pow(2,i,m))

print((p*l)%m)

