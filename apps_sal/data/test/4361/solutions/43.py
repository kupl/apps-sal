n,k=map(int,input().split())
h=sorted([int(input()) for i in range(n)])
c= float('inf')
for i in range(n-k+1):
    c=min(c,h[i+k-1]-h[i])
print(c)
