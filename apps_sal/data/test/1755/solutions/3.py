import sys
input = sys.stdin.readline
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = []
if k:
    b = list(map(int, input().split()))
for i in range(n):
    a[i] -= i
prev = -1
ans = 0
for j in range(k + 1):
    if j < k:
        val = b[j] - 1
        if j and a[prev] > a[val]:
            print(-1)
            quit()
    else:
        val = n
    if val - prev > 1:
        path = [0] * (val - prev - 1)
        arr = [0] * (val - prev)
        found = 0
        for i in range(val - prev - 1):
            if val < n and a[i + prev + 1] > a[val]:
                continue
            elif prev + 1 and a[prev] > a[i + prev + 1]:
                continue
            l = 1
            h = found
            while h >= l:
                m = (l + h + 1) // 2
                if a[arr[m] + prev + 1] <= a[i + prev + 1]:
                    l = m + 1
                else:
                    h = m - 1
            path[i] = arr[l - 1]
            arr[l] = i
            if l > found:
                found = l
        ans += found
    prev = val
print(n - k - ans)
