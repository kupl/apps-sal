A,B,K=list(map(int,input().split()))
ans=0
n=100
while True:
    if A%n==0 and B%n==0:
        ans+=1
        if ans==K:
            print(n)
            return
    n-=1

