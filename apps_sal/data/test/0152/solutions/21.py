(n, m, k) = (int(x) for x in input().split())
(orig, s) = (int(x) for x in input().split())
time1 = [orig] + [int(x) for x in input().split()]
cost1 = [0] + [int(x) for x in input().split()]
make2 = [0] + [int(x) for x in input().split()]
cost2 = [0] + [int(x) for x in input().split()]
ordcost1 = [(x, i) for (i, x) in enumerate(cost1)]
ordcost1.sort()
count = k
best = orig * n
for i in range(m + 1):
    (cost, ind) = ordcost1[i]
    while count > -1 and cost2[count] + cost > s:
        count -= 1
    if count > -1 and time1[ind] * (n - make2[count]) < best:
        best = time1[ind] * (n - make2[count])
print(best)
