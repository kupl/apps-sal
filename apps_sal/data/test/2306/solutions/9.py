# 19/4/17再戦
# -x + a = x + b だと x = (sum)/2で~.5になる可能性がある
# う～～～ん

n = int(input())
ts = list(map(int, input().split()))
vs = list(map(int, input().split()))
sum_t = sum(ts)
n = 2*sum_t+1
max_v = [float("inf")]*n
# 0から右上、-1から左上
for i in range(n):
    max_v[i] = min(i/2, (sum_t-i/2))

# intでtimeは管理するか...
# 0→0, 0.5→1, 1→2 ... i/2→i
t_cnt = 0
for t, v in zip(ts, vs):
    for j in range(2*t+1):
        max_v[t_cnt + j] = min(max_v[t_cnt + j], v)

    # 左側に伸ばしていく
    left = t_cnt
    while left >= 0:
        v_left = v + (t_cnt - left)/2
        if max_v[left] < v_left:
            break
        max_v[left] = v_left
        left -= 1
    # 右側に伸ばしていく
    t_cnt += 2*t
    right = t_cnt
    while right < n:
        v_right = v + (right - t_cnt)/2
        if max_v[right] < v_right:
            break
        max_v[right] = v_right
        right += 1

#print(max_v)
ans = sum(max_v) - (max_v[0]+max_v[-1])/2
print(ans/2)
