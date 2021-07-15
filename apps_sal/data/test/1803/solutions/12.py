input()
a=list(map(int,input().split()))
size=int(input())
for i in range(size):
    x,y=list(map(int,input().split()))
    if x-1>0:
        a[x-2]+=y-1
    if x<len(a):
        a[x]+=a[x-1]-y
    a[x-1]=0
for i in a:
    print(i)

