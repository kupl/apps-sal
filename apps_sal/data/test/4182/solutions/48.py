n,m,x,y=list(map(int,input().split()))
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
mx=max(X)
my=min(Y)
if mx<my:
    for i in range(mx+1,my+1):
        if x<i<=y:
            print("No War")
            return
    print("War")
    
        
    

else:
    print("War")


            

