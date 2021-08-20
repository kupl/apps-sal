(n, d) = list(map(int, input().split()))
t = list(map(int, input().split()))
sum_t = sum(t)
joke_time = (n - 1) * 10
if sum_t + joke_time <= d:
    left = d - (joke_time + sum_t)
    print((joke_time + left) // 5)
else:
    print(-1)
