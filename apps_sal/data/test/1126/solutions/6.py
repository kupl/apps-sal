(N, X, M) = map(int, input().split())
p = [0] * (M + 2)
sum = [0] * (M + 2)
p[X] = 1
sum[1] = X
repeat_start = 0
repeat_end = 0
for i in range(2, N + 1):
    X = X ** 2 % M
    if p[X] != 0:
        repeat_start = p[X]
        repeat_end = i
        break
    else:
        sum[i] = sum[i - 1] + X
        p[X] += i
if repeat_start == 0:
    print(sum[N])
else:
    (repeat_cnt, mod) = divmod(N - repeat_start + 1, repeat_end - repeat_start)
    print(repeat_cnt * (sum[repeat_end - 1] - sum[repeat_start - 1]) + sum[repeat_start + mod - 1])
