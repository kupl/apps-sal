r,d,x=map(int,input().split())
tmp=x
for i in range(10):
    print(r*tmp-d)
    tmp=r*tmp-d
