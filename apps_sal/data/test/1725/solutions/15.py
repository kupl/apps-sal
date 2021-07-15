x,y,n=map(int,input().split())
a=[]
b=[]
for i in range(x):
    a+=list(map(int,input().split()))
r=a[0]%n
count=0
count1=0
for i in a:
    if i%n!=r:
        print(-1)
        return
a.sort()
s=0
x=a[(x*y)//2]
for i in a:
    s+=abs(x-i)//n
print(s)
