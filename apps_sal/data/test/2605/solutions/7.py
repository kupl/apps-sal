n, m = list(map(int,input().split()))
cost = list(map(int,input().split()))
iscapi = [False]*n
capi = list([int(x)-1 for x in input().split()])
#print(capi)
for i in capi:
    iscapi[i]  = True
tot = 0
sumi = 0
for i in range(0,n):
    if not iscapi[i] and not iscapi[(i+1)%n]:
        tot += cost[i]*cost[(i+1)%n]
#print(tot)

price = [cost[i] for i in capi]
#print(price)
for i in range(m-2,-1,-1):
    price[i] += price[i+1]
#print(price)
for i in range(m-1):
    tot += cost[capi[i]]*price[i+1]
#print(tot)

for i in range(n):
    if not iscapi[i]:
        sumi += cost[i]
#print(sumi)
for i in capi:
    tot += cost[i]*sumi
print(tot)
    

    

