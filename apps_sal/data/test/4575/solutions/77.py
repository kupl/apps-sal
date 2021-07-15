N=int(input())
ans=0
D,X=list(map(int,input().split()))
D-=1

for i in range(N):
    ans+=D//int(input())+1
print((ans+X))

