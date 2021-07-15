n,m = input().split()

n=int(n)
m=int(m)

L=[]

least=n//m
remainder=n%m

for i in range(m):
    L.append(least)

for i in range(m):
    if(i==m-1):
        x=""
    else:
        x=" "
    if(remainder>0):
        print(least+1,end=x)
        remainder-=1
    else:
        print(least,end=x)

