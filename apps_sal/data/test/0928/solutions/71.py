(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 0
ans = 0
right = -1
for left in range(n):
    while right < n - 1 and cnt + a[right + 1] < k:
        right = right + 1
        cnt = cnt + a[right]
    if right == n - 1:
        if cnt >= k:
            ans = ans + 1
    elif cnt + a[right + 1] >= k:
        ans = ans + n - right - 1
    cnt = cnt - a[left]
    if right < left:
        right = left - 1
print(ans)
