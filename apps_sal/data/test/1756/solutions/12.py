from bisect import *
n, x = list(map(int, input().split()))
d = list(map(int, input().split()))
d.extend(d)

date_acc = [0]
tot_acc = [0]
for i in range(n * 2):
    date_acc.append(date_acc[i] + d[i])
    tot_acc.append(tot_acc[i] + (d[i] * (d[i] + 1)) // 2)

ans = 0
for i in range(n + 1, 2 * n + 1):
    now = date_acc[i]
    start_i = bisect_left(date_acc, now - x)
    start = date_acc[start_i]
    remain = x - (now - start)
    temp = tot_acc[i] - tot_acc[start_i]
    temp += (remain * (2 * d[start_i - 1] - remain + 1)) // 2
    ans = max(ans, temp)

print(ans)
