n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
left = 1
right = 1
while 1:
    if left * (a[left] - a[left - 1]) <= k:
        k -= left * (a[left] - a[left - 1])
        left += 1
    else:
        print(a[n - right] - a[left - 1] - int(k / left))
        return
    if left + right > n:
        print(0)
        return
    if right * (a[n - right] - a[n - 1 - right]) <= k:
        k -= right * (a[n - right] - a[n - 1 - right])
        right += 1
    else:
        print(a[n - right] - a[left - 1] - int(k / right))
        return
    if left + right > n:
        print(0)
        return
