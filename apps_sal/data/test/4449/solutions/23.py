q=int(input())
while q:
    n=int(input())
    a=input().split()
    for i in range(4*n):
        a[i]=int(a[i])
    a.sort()
    count=0
    value=a[0]*a[4*n-1]
    j=0
    while j<=2*n-2:
        if(a[j]==a[j+1] and a[4*n-j-1]==a[4*n-j-2]):
            if(a[j]*a[4*n-j-1]==value):
                count+=1
        j+=2      
    if(count==n) : print("YES")
    else: print("NO")
    q-=1    
