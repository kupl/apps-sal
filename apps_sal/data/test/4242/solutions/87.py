A,B,K=list(map(int,input().split()))
for x in range(100,0,-1):
    if A%x==0 and B%x==0:
        K-=1
    if K==0:
        print(x)
        break

