t=int(input())
while t:
    n=int(input())
    temp=1
    for i in range(1,50):
        temp+=2**i
        if(n%temp==0):
            print(n//temp)
            break
    t-=1    
