n = int(input())
ts = list(map(int, input().split()))
vs = list(map(int, input().split()))
sum_t = sum(ts)
n = 2 * sum_t + 1
max_v = [float('inf')] * n
for i in range(n):
    max_v[i] = min(i / 2, sum_t - i / 2)
t_cnt = 0
for (t, v) in zip(ts, vs):
    for j in range(2 * t + 1):
        max_v[t_cnt + j] = min(max_v[t_cnt + j], v)
    left = t_cnt
    while left >= 0:
        v_left = v + (t_cnt - left) / 2
        if max_v[left] < v_left:
            break
        max_v[left] = v_left
        left -= 1
    t_cnt += 2 * t
    right = t_cnt
    while right < n:
        v_right = v + (right - t_cnt) / 2
        if max_v[right] < v_right:
            break
        max_v[right] = v_right
        right += 1
ans = sum(max_v) - (max_v[0] + max_v[-1]) / 2
print(ans / 2)
