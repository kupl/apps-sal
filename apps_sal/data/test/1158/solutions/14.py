n, m = map(int, input().split())
c=[0]*200
a= list(map(int, input().split()))
for i in range(n):
    c[a[i]]+=1
summ=0
x=max(c)-max(c)%m
if max(c)%m!=0:
    x+=m
for i in range(len(c)):
    if c[i]!=0:
        summ+=(x-c[i])
print(summ)
