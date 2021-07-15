n=int(input())
a=list(map(int,input().split()))
now=1
for i in a:
    if i==now:
        now+=1
if now==1:
    print(-1)
else:
    print(n-now+1)
