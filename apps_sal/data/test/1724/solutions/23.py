n = int(input())
a = list(map(int, input().split()))
cum_sum = [0] * (n+1)
act_sum = [0] * (n+1)
m = list(input())
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + a[i]
    act_sum[i+1] = act_sum[i]
    if m[i] == '1':
        act_sum[i+1] += a[i]
res = 0
for i in range(n-1, -1, -1):
    if m[i] == '1':
        res = max(res, cum_sum[i] - act_sum[i+1])
print(res + act_sum[n])

