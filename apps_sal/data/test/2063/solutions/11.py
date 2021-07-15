R = lambda: map(int, input().split())
n, m, w = R()
arr = list(R())
l, r = min(arr), min(arr) + m
while l < r:
    mid = (l + r + 1) // 2
    acc, h = 0, [0] * (w + n)
    for i in range(n):
        acc += h[i]
        h[i + w] -= max(0, mid - arr[i] - acc)
        acc -= h[i + w]
    if -sum(h) > m:
        r = mid - 1
    else:
        l = mid
print(l)
