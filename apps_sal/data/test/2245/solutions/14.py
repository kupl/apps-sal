t=int(input())
for x in range(t):
    n,k=list(map(int,input().split()))
    if (k%3)!=0:
        n=n+1
        if(n%3==1):
            print("Bob")
        else:
            print("Alice")
    else:
        
        
        m=(n+1)%(4+3*(k//3-1))
        if(m==0):
            print("Alice")
        else:
            if(m<=(3*(k//3-1))):
                r=m%3
                if(r==1):
                    print("Bob")
                else:
                    print("Alice")
            elif(m==(1+3*(k//3-1))):
                print("Bob")
            else:
                print("Alice")
            


