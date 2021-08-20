import bisect
(n, m, k) = map(int, input().split())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))
sum_a = [0] * (n + 1)
sum_b = [0] * (m + 1)
for i in range(n):
    sum_a[i + 1] = sum_a[i] + aaa[i]
for j in range(m):
    sum_b[j + 1] = sum_b[j] + bbb[j]
ans = 0
for i in range(n + 1):
    if sum_a[i] > k:
        break
    tmp = bisect.bisect_right(sum_b, k - sum_a[i])
    ans = max(ans, i + tmp - 1)
print(ans)
