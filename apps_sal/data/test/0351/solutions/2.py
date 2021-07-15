n,k=list(map(int,input().split()))
x=0
for d in sorted(map(int,input().split())):
    while 2*k<d:
        k*=2
        x+=1
    k=max(k,d)
print(x)

