n=int(input())
d=list(map(int,input().split()))

c=0
for i in range(n-1):
    for j in range(i+1,n):
        c+=(d[i]*d[j])
print(c)
