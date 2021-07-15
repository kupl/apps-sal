K=int(input())
A,B=list(map(int,input().split()))

ans=B//K-(A-1)//K
if ans>0:
    print("OK")
else:
    print("NG")

