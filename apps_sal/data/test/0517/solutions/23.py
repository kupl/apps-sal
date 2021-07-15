__author__ = 'Utena'
n,d,h=map(int,input().split())
ans=[]
if d>2*h:
    print(-1)
    return
elif h==d:
    if h==1 and n>=3:
        print(-1)
        return
    for i in range(2,h+2):
        ans.append([i-1,i])
    for i in range(h+2,n+1):
        ans.append([2,i])
else:
    for i in range(2,h+2):
        ans.append([i-1,i])
    ans.append([1,h+2])
    for i in range(h+3,d+2):
        ans.append([i-1,i])
    for i in range(d+2,n+1):
        ans.append([1,i])
for i in range(n-1):
    print(' '.join(map(str,ans[i])))
