import sys
n,m=list(map(int,sys.stdin.readline().split()))

Colors=[0]*(n+1)

for i in range(m):
    a,b,c=list(map(int,sys.stdin.readline().split()))
    Z=[a,b,c]
    Q=[1,2,3]
    if(Colors[a]!=0):
        Z.remove(a)
        Q.remove(Colors[a])
    if(Colors[b]!=0):
        Z.remove(b)
        Q.remove(Colors[b])
    if(Colors[c]!=0):
        Z.remove(c)
        Q.remove(Colors[c])
    for i in range(len(Z)):
        Colors[Z[i]]=Q[i]


Ans=""
Ans+=str(Colors[1])
for i in range(2,n+1):
    Ans+=" "+str(Colors[i])
sys.stdout.write(Ans)
    

