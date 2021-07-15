a,b = list(map(int,input().split()))
mini = 1
maxi = 10000
for i in range(b):
    x,y = list(map(int,input().split()))
    if y==1:
        mini = max(mini,x)
    else:
        mx = (x-1)//(y-1) 
        mn=(x-1)//y+1
        if mn*y>=x:
            mini = max(mini,mn)
        else:
            mini = max(mini,mn+1)
        if mx*y>=x:
            maxi = min(maxi,mx)
if (a-1)//maxi==(a-1)//mini:
    print((a-1)//maxi+1)
else:
    print(-1)

