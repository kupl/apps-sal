n,k=map(int,input().split())
h=n//2
d=h//(k+1)
c=d*k
r=n-(d+c)
print(d,c,r)
