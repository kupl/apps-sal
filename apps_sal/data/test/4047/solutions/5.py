n=int(input())
l1=list(map(int,input().split()))
x=0
for item in l1:
    if item%2==0:
        x+=1
print(min(x,n-x))
