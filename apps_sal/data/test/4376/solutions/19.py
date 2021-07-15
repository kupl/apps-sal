read=lambda:map(int,input().split())
n,m=read()
a=list(read())
b=list(read())
pos=0
pre=0
for i in b:
    d=0
    while True:
        d=i-1-pre
        if d>=a[pos]: pre+=a[pos];pos+=1
        else: break
    print(pos+1,d+1)
