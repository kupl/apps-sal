k=int(input())
a,b=map(int,input().split())
ans=False
for x in range(a,b+1):
    if x%k==0:ans=True
if(ans):print("OK")
else :print("NG")
