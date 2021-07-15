n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
counter=0
b.sort(reverse=True)
c=[]
for i in range(n):
    c.append(a[i]*b[i])
tot=[]
for i in range(n):
    x=(min(i,n-i-1)+1)
    tot.append((x*(x+1)+(n-2*x)*x)*a[i])
tot.sort()
for i in range(n):
    counter+=tot[i]*b[i]
    
print(counter%998244353)

