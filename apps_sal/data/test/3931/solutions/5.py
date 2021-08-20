(n, a, b, k, f) = list(map(int, input().split()))
totalCost = {}
lastStop = ''
total = 0
for i in range(n):
    (s1, s2) = input().split()
    cost = a if lastStop != s1 else b
    key = (min(s1, s2), max(s1, s2))
    if key not in totalCost:
        totalCost[key] = cost
    else:
        totalCost[key] += cost
    total += cost
    lastStop = s2
sortedTotalCost = [(totalCost[key], key[0], key[1]) for key in totalCost]
sortedTotalCost.sort(reverse=True)
i = 0
while i < len(sortedTotalCost) and k > 0 and (sortedTotalCost[i][0] > f):
    total -= sortedTotalCost[i][0]
    total += f
    k -= 1
    i += 1
print(total)
