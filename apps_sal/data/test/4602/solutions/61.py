N=int(input())
K=int(input())
x=list(map(int,input().split()))
tot=0
for i in range(N):
    if abs(x[i]-K)<x[i]:
        tot+=2*(abs(x[i]-K))
    else:
        tot+=2*x[i]
print(tot)
