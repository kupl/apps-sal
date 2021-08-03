n, x = map(int, input().split())
a = [int(_) for _ in input().split()]
ans = max(0, a[0] - x)
a[0] -= ans
for i in range(n - 1):
    if a[i] + a[i + 1] > x:
        val = a[i] + a[i + 1] - x
        a[i + 1] -= val
        ans += val
print(ans)
