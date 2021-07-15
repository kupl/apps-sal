x,n=map(int,input().split())
l=list(map(int,input().split()))
flag=0
i=0
while flag==0:
    if x-i not in l:
        flag=1
        ansa=x-i
    i+=1
flag=0
i=0
while flag==0:
    if x+i not in l:
        flag=1
        ansb=x+i
    i+=1
if abs(ansa-x)<=abs(ansb-x):
    print(ansa)
else:
    print(ansb)
