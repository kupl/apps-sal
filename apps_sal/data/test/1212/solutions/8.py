def readInput():
    return [int(x) for x in input().split()]


inputdata = readInput()
data = readInput()

n = inputdata[0]
k = inputdata[1]

sums = list(range(n))
for i in range(n):
    sums[i] = data[i]
    if (i > 0):
        sums[i] += sums[i - 1]

index = -1
minVal = -1

i = 0
while i + k - 1 <= n - 1:
    if (index == -1):
        index = 0
        minVal = sums[k - 1]
    else:
        curr = sums[i + k - 1] - sums[i - 1]
        if (curr < minVal):
            minVal = curr
            index = i
    i += 1

print(index + 1)
