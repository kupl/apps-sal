I=lambda:list(map(int,input().split()))
n,m=I();a=I();b=I()
i=j=0
while(i<n and j<m):
    i+=1*(a[i]<=b[j]);j+=1
print(n-i)
