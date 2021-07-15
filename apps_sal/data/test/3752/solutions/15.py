k,d,t=list(map(int,input().split()))
d=((k+d-1)//d)*d
n=2*t//(d+k)
x=2*t%(d+k)
if (x<=2*k):
    ans=x/2+d*n
else:
    ans=x-k+d*n
print(ans)
    

