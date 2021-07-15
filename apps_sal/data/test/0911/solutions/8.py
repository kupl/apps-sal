m,c=list(map(int,input().split()))
p=list(map(int,input().split()))
n=list(map(int,input().split()))

sum1,sum2,sm=0,0,0

for i in range(m):
    sm+=n[i]
    sum1=sum1+max(0,p[i]-c*sm )

sm=0
i=m-1
while i>=0:
    sm+=n[i]
    sum2=sum2+max(0,p[i]-c*sm)
    i-=1
if sum1>sum2:
    print("Limak")
elif sum2>sum1:
    print("Radewoosh")
elif sum1 == sum2 :
    print("Tie")

