d=dict()
for i in range(1,101):
    d[i]=0
n=int(input())
for _ in range(n):
    a=list(map(int,input().split()))
    for i in range(1,len(a)):
        d[a[i]]+=1
for i in range(1,101):
    if d[i]==n:
        print(i,end=" ")
