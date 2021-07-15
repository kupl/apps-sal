n,x,y=list(map(int,input().split()))
s=set()
k=0
for i in range(n):
    a,b=list(map(int,input().split()))
    if b-y!=0:
        s.add((x-a)/(y-b))
    else:
        k=1
print(len(s)+k)


