(n, n1, n2) = list(map(int, input().split()))
line = list(map(int, input().split()))
line.sort(reverse=True)
mi = min(n1, n2)
ma = max(n1, n2)
i = 0
minSum = 0
maxSum = 0
for x in range(mi):
    minSum = minSum + line[i]
    i = i + 1
for x in range(ma):
    maxSum = maxSum + line[i]
    i = i + 1
print(minSum / mi + maxSum / ma)
