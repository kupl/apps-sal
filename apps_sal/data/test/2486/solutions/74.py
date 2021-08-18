n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a = sorted(a)
sum_a = 0
ans = 0
for i in range(n - 1, -1, -1):
    if sum_a + a[i] < k:
        sum_a += a[i]
        ans += 1
    else:
        ans = 0
print(ans)
