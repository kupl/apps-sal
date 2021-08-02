n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = list(map(int, input().split()))

if k >= 2:
    m = min(d[: -1])
    print(max(sum(a) - m, a[-1] - d[-1], 0))
elif k == 0:
    rightans = [0] * n
    cursum = 0
    ans = 0
    for i in range(n - 1, -1, -1):
        cursum += a[i]
        rightans[i] = max(cursum - d[i], 0)
    print(max(rightans))
else:
    leftd = int(1e9)
    leftsum = 0
    rightans = [0] * n
    cursum = 0
    ans = 0
    for i in range(n - 1, -1, -1):
        cursum += a[i]
        rightans[i] = max(cursum - d[i], 0)
    for i in range(n - 1, 0, -1):
        rightans[i - 1] = max(rightans[i - 1], rightans[i])
    for i in range(n - 1):
        leftd = min(leftd, d[i])
        leftsum += a[i]
        curans = max(leftsum - leftd, 0) + rightans[i + 1]
        ans = max(ans, curans)

    cursum = 0
    rightmin = int(1e9)
    for i in range(n - 1, -1, -1):
        cursum += a[i]
        ans = max(ans, cursum - rightmin - d[i])
        rightmin = min(rightmin, a[i])
    print(ans)
