n=int(input())
a=[]
for i in range(n):
    a.append(input())
k=0
for i in range(1,n):
    if int(a[i-1])!=int(a[i]):
        k+=1    
print(k+1)                
       

