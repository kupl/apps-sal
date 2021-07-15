n=int(input())
a=list(map(int,input().split()))
c=[]
for j in range(n):
    l=0
    for i in range(j,len(a)):
        l=l^a[i]
        c.append(l)
print(max(c))
