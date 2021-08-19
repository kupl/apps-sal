(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
roomsT = 0
currD = -1
for x in range(m):
    toFind = b[x]
    while roomsT < b[x] and currD < n:
        currD += 1
        roomsT += a[currD]
    roomsT -= a[currD]
    currD -= 1
    tempR = toFind - roomsT
    print(currD + 2, tempR)
