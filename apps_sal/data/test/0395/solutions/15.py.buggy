a = list(map(int, input().split()))
for i in range(1 << 6):
    currsum = 0
    currcnt = 0
    for j in range(6):
        if ((i >> j) & 1) != 0:
            currsum += a[j]
            currcnt += 1
        else:
            currsum -= a[j]
    if currsum == 0 and currcnt == 3:
        print('YES')
        return
print('NO')
