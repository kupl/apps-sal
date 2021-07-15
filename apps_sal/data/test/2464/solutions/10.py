def addEdge(arr: [], x, y):
    x, y = getRoot(arr, x), getRoot(arr, y)
    if arr[x] <= arr[y]:
        arr[x] += arr[y]
        arr[y] = x
    else:
        arr[y] += arr[x]
        arr[x] = y


def getRoot(arr: [], id):
    while arr[id] > 0:
        id = arr[id]
    return id


def solve(zeroArr: [], oneArr: []):
    Ans = 0
    for i in range(1, len(zeroArr)):
        if zeroArr[i] < 0:
            Ans += zeroArr[i] * (-1) * (zeroArr[i] * (-1) - 1)
        if oneArr[i] < 0:
            Ans += oneArr[i] * (-1) * (oneArr[i] * (-1) - 1)
        if (zeroArr[i] != -1 and oneArr[i] != -1):
            one, zero = getRoot(oneArr, i), getRoot(zeroArr, i)
            Ans += (oneArr[one] * (-1) - 1) * (zeroArr[zero] * (-1) - 1)
    return Ans

n = int(input())
zeroArr, oneArr = [-1] * (n + 1), [-1] * (n + 1)
while n > 1:
    a, b, w = [int(x) for x in input().split()]
    if w == 0:
        addEdge(zeroArr, a, b)
    else:
        addEdge(oneArr, a, b)
    n -= 1
print(solve(zeroArr, oneArr))

