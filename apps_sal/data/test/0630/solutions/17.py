def read():
    return list(map(int,input().split()))
n,k=read()
a=read()
b=[min(k,n-1)+1]
for i in range(1,n):
    if a[i]==0:
        b.append(min(i,k)+1+min(n-i-1,k))
    else:
        b.append(b[a[i]-1]-min(k,n-a[i])+min(i-a[i],2*k)+min(n-i-1,k)+1)
print(*b)

    
        

