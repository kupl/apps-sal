n, h = map(int, input().split())
brr = [0] * n
for i in range(n):
    brr[i] = list(map(int, input().split()))
arr = [0] * (2 * n)
for i in range(n):
    arr[2 * i] = brr[i][0]
    arr[2 * i + 1] = brr[i][1]
if n == 1:
    print(arr[1] - arr[0] + h)
    return
if h == 1:
    dis = 0
    for i in range(1, 2 * n, 2):
        dis = max(dis, arr[i] - arr[i - 1])
    print(dis + 1)
    return

diff = [0] * (n - 1)
add = [0] * (n)
for i in range(n - 1):
    diff[i] = diff[i - 1] + arr[2 * i + 2] - arr[2 * i + 1]
    add[i] = add[i - 1] + arr[2 * i + 1] - arr[2 * i]
add[n - 1] = add[n - 2] + arr[2 * n - 1] - arr[2 * n - 2]
ans = 0
for i in range(0, 2 * n, 2):
    j = i // 2
    lo = j
    hi = n - 2
    pre = diff[lo - 1]
    if lo == 0:
        pre = 0
    while(lo <= hi):
        mid = (lo + hi) // 2
        if diff[mid] - pre <= h:
            lo = mid + 1
            if mid == n - 2 or diff[mid + 1] - pre > h:
                break
        else:
            hi = mid - 1
    ext = h - diff[mid] + pre
    if ext != 0:
        ans = max(ans, arr[(mid * 2) + 3] + ext - arr[i])
    else:
        ans = max(ans, arr[(mid * 2) + 2] - arr[i])
print(ans)
