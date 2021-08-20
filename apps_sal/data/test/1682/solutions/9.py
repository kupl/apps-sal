from sys import stdin, stdout
(n, k) = list(map(int, stdin.readline().rstrip().split()))
a = stdin.readline().rstrip().split()
a = [int(num) for num in a]
b = stdin.readline().rstrip().split()
b = [int(num) for num in b]
costDiff = [b[i] - a[i] for i in range(n)]
sortedCostDiff = sorted(costDiff, reverse=True)
savingMade = len([i for i in costDiff if i >= 0])
if savingMade >= k:
    totalSpend = 0
    for i in range(n):
        totalSpend += min([a[i], b[i]])
else:
    maxCost = sortedCostDiff[k - 1]
    cutoffSortedDiff = sortedCostDiff[:k]
    minCount = cutoffSortedDiff.count(maxCost)
    totalSpend = 0
    for i in range(n):
        if b[i] - a[i] > maxCost:
            totalSpend += a[i]
        elif b[i] - a[i] == maxCost and minCount > 0:
            totalSpend += a[i]
            minCount -= 1
        else:
            totalSpend += b[i]
print(totalSpend)
