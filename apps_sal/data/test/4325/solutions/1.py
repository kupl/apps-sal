N,X,T=map(int,input().split())
for i in range(1,1001):
    if X*i>=N:
        print(i*T)
        return
