n, d = map(int, input().split())
t = list(map(int, input().split()))
sum_time = (n - 1) * 10 + sum(t)
if sum_time > d:
    print(-1)
else:
    res_time = d - sum_time
    cnt = res_time / 5 + (n - 1) * 2
    print(int(cnt))
