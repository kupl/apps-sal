import heapq

inp = list(map(int, input().split()))
n = inp[0]
k = inp[1]
x = inp[2]

a = [int(i) for i in input().strip().split(' ')]

isPositive = True
nodes = [[abs(val), val, index] for index, val in enumerate(a)]

for el in a:
    if el < 0:
        isPositive = not isPositive

heapq.heapify(nodes)

for i in range(k):
    minNode = nodes[0]
    val = minNode[1]
    isCurPositive = val >= 0
    newVal = val
    if isPositive == isCurPositive:
        newVal -= x
    else:
        newVal += x

    minNode[1] = newVal
    if val >= 0 > newVal or val < 0 <= newVal:
        isPositive = not isPositive

    heapq.heapreplace(nodes, [abs(newVal), newVal, minNode[2]])

result = [None] * n
for node in nodes:
    result[node[2]] = str(node[1])

print(" ".join(result))
