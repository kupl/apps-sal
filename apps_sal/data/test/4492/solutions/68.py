(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    num = x
    num2 = a[i - 1] + a[i] - x
    if num2 > 0:
        ans += num2
        a[i] = max(a[i] - num2, 0)
print(ans)
