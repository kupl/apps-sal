(n, m) = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
arr = sorted(arr, reverse=True)
low = 1
high = n


def check(k, m):
    if m > 0:
        l = 0
        z = 0
        for i in range(n):
            m -= max(0, arr[i] - l)
            z += 1
            if z == k:
                z = 0
                l += 1
    if m <= 0:
        return 1
    else:
        return 0


ans = []
while high >= low:
    mid = low + (high - low) // 2
    if check(mid, m):
        ans.append(mid)
        high = mid - 1
    else:
        low = mid + 1
if len(ans) > 0:
    print(min(ans))
else:
    print(-1)
