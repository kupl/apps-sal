n=int(input())
L=list(map(int,input().split()))
ans=['']*n
revL=[0]*n
ans[-1]='B'
for i in range(n):
    revL[L[i]-1]=i+1
for i in range(n-2,-1,-1):
    t=revL[i]-1
    counter='B'
    for j in range(t,-1,-i-1):
        if j==t:continue
        if ans[L[j]-1]=='B':
            counter='A'
            break
    if counter!='A':
        for k in range(t,n,i+1):
            if k==t:continue
            if ans[L[k]-1]=='B':
                counter='A'
                break
    ans[i]=counter
for i in range(n):
    print(ans[L[i]-1],sep='',end='')
