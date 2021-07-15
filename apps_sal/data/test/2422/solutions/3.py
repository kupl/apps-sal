t=int(input())
for you in range(t):
    n=int(input())
    if(n==1 or n==2 or n==4):
        print(-1)
        continue
    if(n==3):
        print(1,0,0)
        continue
    z=n%3
    if(z==0):
        print(n//3,0,0)
    if(z==1):
        print((n-7)//3,0,1)
    if(z==2):
        print((n-5)//3,1,0)

