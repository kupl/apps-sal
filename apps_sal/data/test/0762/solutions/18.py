n, c = [int(x) for x in input().split()]
ns = [int(x)for x in input().split()]
odd = 0
cost = []
for i in range(n):
    if (ns[i] & 1) == 1:
        odd += 1
    else:
        odd -= 1
    if odd == 0:
        if i < n - 1:
            cost.append(abs(ns[i + 1] - ns[i]))
cost.sort()
sum = 0
p = False
for i in range(len(cost)):
    sum += cost[i]
    if sum > c:
        print(i)
        p = True
        break
if not p:
    print(len(cost))
