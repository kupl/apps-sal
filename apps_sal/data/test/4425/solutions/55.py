N, K = map(int, input().split())
pro=0.0
for i in range(1,N+1):
    n=i
    j=0
    while(True):
        if n >= K:
            break
        n=n*2
        j=j+1
    pro=pro+(1/N)*(0.5)**(j)
print(pro)
