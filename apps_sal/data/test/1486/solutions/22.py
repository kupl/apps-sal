n = int(input())
a = list(map(int, input().split()))

for i, x in enumerate(a):
    mn = int(2e9)
    mx = int(-2e9)
    if i > 0:
        mn = min(mn, x - a[i - 1])
        mx = max(mx, x - a[0])
    if i < n - 1:
        mn = min(mn, a[i + 1] - x)
        mx = max(mx, a[-1] - x)
    print(mn, mx)

