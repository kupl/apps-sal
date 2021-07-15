n,t=list(map(int,input().split()))
cost=1001
for i in range(n):
    ci,ti=list(map(int,input().split()))
    if ti<=t and ci<cost:
        cost=ci
if cost==1001:
    print('TLE')
else:
    print(cost)

