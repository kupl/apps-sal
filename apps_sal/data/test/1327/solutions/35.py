(n, m) = map(int, input().split())
value_sum = [[0] * n for i in range(8)]
ans = [0] * 8
for i in range(n):
    value = list(map(int, input().split()))
    for j in range(8):
        for k in range(3):
            if j >> k & 1:
                value_sum[j][i] += value[k]
            else:
                value_sum[j][i] -= value[k]
for i in range(8):
    value_sum[i].sort(reverse=True)
    ans[i] = sum(value_sum[i][:m])
print(max(ans))
