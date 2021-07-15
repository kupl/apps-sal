K=int(input())
n=1
k=0
x=[]
y=x.append
while(n<=10**15):
    plus=10**k
    if n>=1350*plus:
        n+=9*plus
        k+=1
        plus*=10
    y([n,n/sum(map(int,list(str(n))))])
    n+=plus
x2=[]
y2=x2.append
min_=10**15
for i in range(len(x)-1,-1,-1):
    if x[i][1]<=min_:
        y2(x[i][0])
        min_=x[i][1]
x2=list(reversed(x2))
for i in range(K):
    print(x2[i])
