def check(arr, d, mm):
    ss = 0
    k = -1
    for i in range(n):
        if i % d == 0:
            k += 1
        ss += max(0, arr[i] - k)
    if ss >= mm:
        return True
    else:
        return False


(n, m) = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
s = 1
e = n
ans = 1000000000000000000000
while s <= e:
    mid = (s + e) // 2
    if check(arr, mid, m):
        ans = min(ans, mid)
        e = mid - 1
    else:
        s = mid + 1
if ans == 1000000000000000000000:
    ans = -1
print(ans)
