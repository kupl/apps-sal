n,k =list(map(int,input().split()))

a=[int(x) for x in input().split()]
bag=a[0]//k
remain=a[0]%k
for i in range(1,n):
    tk=a[i]+remain
    remain=tk%k
    if remain>a[i]:
        bag+=1
        remain=0
    else:
        bag+=tk//k
    
if remain==0:
    print(bag)
   
        
else:  
        
    print(bag+1)        

