N=int(input())
K=int(input())
now=1
for i in range(N):
    now=min(now*2,now+K)
print(now)
