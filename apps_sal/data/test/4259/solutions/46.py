K=int(input())
A,B=map(int,input().split())
ans=0
i=1
while K*i<=1000:
    if A<=K*i and K*i<=B:
        ans=1
        break
    i+=1
if ans==1:
    print("OK")
else:
    print("NG")
