# Fence

data = input().split(" ")
n = int(data[0])
k = int(data[1])
minIndex = 1
minCost = 0
heights = input().split(" ")
heights = [int(x) for x in heights]
for j in range(k):
    minCost += heights[0 + j]

cost = minCost
for i in range(1, len(heights) - k + 1):
    cost = cost - heights[i - 1] + heights[i + k - 1]
    if cost < minCost:
        minCost = cost
        minIndex = i + 1
print(minIndex)
