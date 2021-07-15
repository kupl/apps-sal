import sys
input = sys.stdin.readline

n=int(input())
s=input().strip()

AB=[tuple(map(int,input().split())) for i in range(n)]

ANS=[[0]*n for i in range(3000)]

for i in range(n):
    k=int(s[i])
    a,b=AB[i]

    t=0
    while t<3000:
        if t>=b and (t-b)%a==0:
            k=1-k
            
        ANS[t][i]=k
        t+=1


    
A=0
for t in range(3000):
    A=max(A,sum(ANS[t]))

print(A)

