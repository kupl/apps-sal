n, t = map(int, input().split())
tm = list(map(int, input().split()))
start_time = -1
stop_time = -1
ans = 0
for i in range(0, n):
    if start_time <= tm[i] <= stop_time:
        stop_time += (t + tm[i]) - stop_time
    else:
        ans += (stop_time - start_time)
        start_time = tm[i]
        stop_time = tm[i] + t
    if i == n - 1:
        ans += (stop_time - start_time)
print(ans)
