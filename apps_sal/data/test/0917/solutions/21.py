ints = [int(x) for x in input().split()]
n = ints[0]
h = ints[1]
m = ints[2]
maxheights = [h for i in range(n)]
for i in range(m):
    integers = [int(x) for x in input().split()]
    for j in range(integers[0] - 1, integers[1]):
        maxheights[j] = min(maxheights[j], integers[2])
maxSum = 0
for i in range(n):
    maxSum = maxSum + maxheights[i] ** 2
print(maxSum)
