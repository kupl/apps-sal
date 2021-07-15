n,m,x = map(int,input().split())
a = [int(s) for s in input().split()]
cost = []
count = 0

for i in range(x,n):
    if a.count(i) == 1:
        count += 1
cost.append(count)
count = 0
c = range(0,x)
for i in reversed(c):
    if a.count(i) == 1:
        count += 1
cost.append(count)
print(min(cost))
