# import numpy as np

H, W, M = list(map(int, input().split()))
#map_ = np.zeros((H, W), dtype=np.bool)

h_sum = [0] * H
w_sum = [0] * W
point_list = set()

for _ in range(M):
    h, w = list(map(int, input().split()))
    # map_[h-1, w-1] = 1
    point_list.add((h - 1, w - 1))
    h_sum[h - 1] += 1
    w_sum[w - 1] += 1

h_max = max(h_sum)
w_max = max(w_sum)

h_argmax = set()
w_argmax = set()

for i, h in enumerate(h_sum):
    if h == h_max:
        h_argmax.add(i)

for i, w in enumerate(w_sum):
    if w == w_max:
        w_argmax.add(i)

ans = h_max + w_max

for h in h_argmax:
    for w in w_argmax:
        if (h, w) not in point_list:
            # if map_[h, w] == 0:
            print(ans)
            return
print((ans - 1))
