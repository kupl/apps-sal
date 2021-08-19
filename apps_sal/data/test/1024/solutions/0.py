def getSum(BITree, index):
    sum = 0
    while index > 0:
        sum += BITree[index]
        index -= index & -index
    return sum


def updateBIT(BITree, n, index, val):
    while index <= n:
        BITree[index] += val
        index += index & -index


def getInvCount(arr, n):
    invcount = 0
    maxElement = max(arr)
    BIT = [0] * (maxElement + 1)
    for i in range(1, maxElement + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
        invcount += getSum(BIT, arr[i] - 1)
        updateBIT(BIT, maxElement, arr[i], 1)
    return invcount


def getInvCountAdv(arr, n):
    invcount = 0
    maxElement = max(arr)
    BIT = [0] * (maxElement + 1)
    for i in range(1, maxElement + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
        invcount += (i + 1) * getSum(BIT, arr[i] - 1)
        updateBIT(BIT, maxElement, arr[i], n - i)
    return invcount


n = int(input())
a = list(map(int, input().split()))
InvCount = getInvCount(a, n)
InvCountAdv = getInvCountAdv(a, n)
thirdSum = 0
for i in range(1, n + 1):
    thirdSum += i * (i - 1) * (n - i + 1) / 2
print(InvCount - InvCountAdv / (n * (n + 1)) * 2 + thirdSum / (n * (n + 1)))
