n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
res = 10 ** 10
tmp_sum = 0
for i in range(n - 1):
    tmp_sum += a[i]
    res = min(res, abs(tmp_sum - (sum_a - tmp_sum)))

print(res)
