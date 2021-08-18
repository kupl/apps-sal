n = int(input())
a = list(map(int, input().split()))

l = 0
SUM, XOR = 0, 0
ans = 0
for r in range(n):
    SUM += a[r]
    XOR ^= a[r]
    if SUM == XOR:
        ans += (r - l + 1)
    else:
        while l <= r and SUM != XOR:
            SUM -= a[l]
            XOR ^= a[l]
            l += 1
        ans += (r - l + 1)

print(ans)
