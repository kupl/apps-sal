n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
s = 0

r = 0
for l in range(n):
    while s < k:
        if r == n:
            break
        s += a[r]
        r += 1
    if s < k:
        break
    ans += n-r+1
    s -= a[l]
print(ans)

