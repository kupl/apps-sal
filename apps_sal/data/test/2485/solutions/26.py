from collections import Counter


H, W, M, *hw = map(int, open(0).read().split())
h_cnt = Counter(hw[::2])
w_cnt = Counter(hw[1::2])
h_max = h_cnt.most_common(1)[0][1]
w_max = w_cnt.most_common(1)[0][1]

not_on_bomb = sum(1 for k, v in h_cnt.items() if v == h_max)
not_on_bomb *= sum(1 for k, v in w_cnt.items() if v == w_max)
for h, w in zip(*[iter(hw)] * 2):
    if h_cnt[h] == h_max and w_cnt[w] == w_max:
        not_on_bomb -= 1

ans = h_max + w_max
print(ans) if not_on_bomb else print(ans - 1)
