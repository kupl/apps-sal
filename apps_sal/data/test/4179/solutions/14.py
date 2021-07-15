n,m,c=list(map(int, input().split()))
b=[int(i) for i in input().split()]

count=0
for i in range(n):
    a=[int(i) for i in input().split()]
    sum=c
    for j in range(m):
        sum+=a[j]*b[j]
    
    if sum>0:
        count+=1
        
print(count)

