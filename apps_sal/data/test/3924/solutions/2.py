(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0
pre = 0
for i in range(n):
    if pre != 0:
        ans += 1
        a[i] -= k - pre
        if a[i] < 0:
            a[i] = 0
    ans += a[i] // k
    pre = a[i] - a[i] // k * k
if pre != 0:
    ans += 1
print(ans)
