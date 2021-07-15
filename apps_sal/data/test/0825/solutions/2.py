n=int(input())
def f(x):
    z=1
    while not(z*(z+1)<=2*x<(z+1)*(z+2)):
        z+=1
    return z

x=[-1]*(10**6+1) #2以上の自然数に対して最小の素因数を表す
x[0]=0
x[1]=1
i=2
prime=[]
while i<=10**6:
    if x[i]==-1:
        x[i]=i
        prime.append(i)
    for j in prime:
        if i*j>10**6 or j>x[i]:break
        x[j*i]=j
    i+=1
if n==1:
    print((0))
    return

a=[]
q=0
for i in range(len(prime)):
    p=prime[i]
    while n%p==0:
        q+=1
        n=n//p
    if q>0:a.append(q)
    q=0

ans=0
for i in range(len(a)):
    ans+=f(a[i])
print((ans if n==1 else ans+1))

