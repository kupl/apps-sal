from functools import reduce
(n, k, m) = list(map(int, input().split()))
t = list(map(int, input().split()))
t.sort()
sum = reduce(lambda x, y: x + y, t)
mx = 0
full = 0
while full <= n and full * sum <= m:
    cnt = full * k + full
    free_time = m - sum * full
    for time in t:
        tasks = min(n - full, free_time // time)
        cnt += tasks
        free_time -= tasks * time
    mx = max(mx, cnt)
    full += 1
print(mx)
