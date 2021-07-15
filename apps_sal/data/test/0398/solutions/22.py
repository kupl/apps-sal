n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
c=0
for i in range(n-2) :
    if l[i]+l[i+1]>l[i+2] :
        c=1
        break
if c==1 :
    print('YES')
else :
    print('NO')

