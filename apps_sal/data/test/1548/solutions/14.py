n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
x,y=0,0
for i in range(n//2):
    x += a[i]
for i in range(n//2,n):
    y += a[i]
print(pow(x,2)+pow(y,2))
