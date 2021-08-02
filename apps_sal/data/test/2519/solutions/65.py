n, k = [int(i) for i in input().split()]
p = [(int(i) + 1) / 2 for i in input().split()]

ans = 0
sum_num = sum(p[:k])
for i in range(n - k + 1):
    if i == 0:
        sum_num = sum(p[:k])
    else:
        sum_num += p[i + k - 1] - p[i - 1]
    ans = max(ans, sum_num)
print(ans)
