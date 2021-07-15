n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
m = 0
for i in range(0,n-k+1):
    x = sum(a[i:k+i-1])
    y = k-1
    for j in range(k+i,n+1):
        x +=a[j-1]
        y +=1
        if x/y > m:
            m = x/y
print(m)

