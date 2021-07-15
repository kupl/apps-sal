n = int(input())
P = list(map(int, input().split()))

num_idx = [0]*(n+1)

# 自分のidxからみて右側で，自身の値より大きな値をもつ，一番近いidx
right_idx_over_current_pos = list(range(1, n+1)) + [n, n]
# 自分のidxからみて左側で，自身の値より大きな値をもつ，一番近いidx
left_idx_over_current_pos = list(range(-1, n-1)) + [-1, -1]

# 1から見ていくとすると，上記2つとも，自分のすぐ隣のidxがそのまま該当する

for idx, num in enumerate(P):
    num_idx[num] = idx

ans = 0
for num in range(1, n+1):  # 小さいほうから決める
    now = num_idx[num]
    r1 = right_idx_over_current_pos[now]
    r2 = right_idx_over_current_pos[r1]
    l1 = left_idx_over_current_pos[now]
    l2 = left_idx_over_current_pos[l1]

    r_pattern = (r2-r1) * (now-l1)
    l_pattern = (l1-l2) * (r1-now)

    right_idx_over_current_pos[l1] = r1  # l1にある値 > nowからr1までにある値 なので nowをスキップして r1までいける
    left_idx_over_current_pos[r1] = l1  # 上の左向きver
    ans += (r_pattern + l_pattern) * num

print(ans)

