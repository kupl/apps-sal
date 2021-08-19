(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
ans = 10 ** 13
m -= 1
for i in range(n):
    if a[i] != 0 and a[i] <= k and (ans > abs(i - m) * 10):
        ans = 10 * abs(i - m)
print(ans)
