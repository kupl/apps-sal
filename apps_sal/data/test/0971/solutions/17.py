n,b,d=map(int,input().split())
lis=list(map(int,input().split()))
empty=0
t1=0
t2=0
for i in lis:
    if i>b:
        continue
    t1+=i
    if t1>d:
        empty+=1
        t1=0
print(empty)
