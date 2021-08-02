n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = float('inf')

for i in range(0, n - k + 1):
    b = a[i]
    c = a[i + k - 1]
    if c <= 0:
        ans = min(ans, abs(b))
    elif b >= 0:
        ans = min(ans, abs(c))
    else:
        ans = min(ans, abs(c) + abs(b) * 2, abs(c) * 2 + abs(b))

print(ans)
