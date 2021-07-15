n,k = list(map(int, input().split()))
jobs = [int(s) for s in input().split()]
cost = [int(s) for s in input().split()]
d=[]
c=[0]*(k+1)
for i in range(n):
    d.append((cost[i], jobs[i]))
    c[jobs[i]] += 1
rest = 0
for i in range(1,k+1):
    if c[i] == 0:
        rest +=1
d.sort(key = lambda x: x[0])
allcost = 0
i = 0
while rest > 0:
    if c[d[i][1]]>1:
        c[d[i][1]] -=1
        allcost += d[i][0]
        rest-=1
    i+=1
print(allcost)

