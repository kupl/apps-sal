n=int(input())
S=input()
l=list(map(int,input().split()))
i=0
c=1
while i>=0 or i>=n-1 :
    if S[i]=='>' and i+l[i]>n-1 :
        c=1
        break
    if S[i]=='<' and i-l[i]<0 :
        c=1
        break
    if l[i]==0 :
        c=0
        break
    d=l[i]
    l[i]=0
    if S[i]=='>' :
        i=i+d
    else :
        i=i-d
if c==1 :
    print('FINITE')
else :
    print('INFINITE')

