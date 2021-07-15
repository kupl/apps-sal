n, k = list(map(int, input().split()))
m = k // 2 + 1
l = m - 1
if k % 2 == 0:
    l -= 1
print(max(0, min(l, n - m + 1)))

