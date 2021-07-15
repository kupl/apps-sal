# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if n==2 or n==3 :
        print(-1)
        #break
    elif n==4:
        print("3 1 4 2")
    else:
        c=1
        if n%2==0:
            for i in range(1,n,2):
                print(i,end=" ")
            if n-4>0:
                print(n-4,end=" ")
            for i in range(n,0,-2):
                if i !=(n-4) and i!=0:
                    print(i,end=" ")
        else:
            for i in range(1,n+1,2):
                print(i,end=" ")
            if n-3>0:
                print(n-3,end=" ")
            for i in range(n-1,0,-2):
                if i!=(n-3) and i!=0:
                    print(i,end=" ")
            
            
        print()
    
        
