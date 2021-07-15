n=int(input())
x=list(map(int,input().split()))

a=x[0]
c=[]

for i in range(1,n):
    if x[i]<a:
        c.append(a-x[i])
    if x[i]>a:
        a=x[i]
print(sum(c))
