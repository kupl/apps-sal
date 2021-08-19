(n, m, w) = map(int, input().split())
a = list(map(int, input().split()))


def check(x):
    b = [0] * n
    cur = cnt = 0
    for i in range(n):
        if i - w >= 0:
            cur -= b[i - w]
        if a[i] + cur < x:
            b[i] = x - a[i] - cur
            cur += b[i]
            cnt += b[i]
        if cnt > m:
            return 0
    return 1


left = 1
right = 1000000000.0 + 1000000.0
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(int(ans))
