#!/usr/bin/env python3
import numpy as np

h, w = list(map(int, input().split()))

s = np.array([list(input()) for _ in range(h)]) == "."

ups = np.zeros((h, w), dtype=int)
downs = np.zeros((h, w), dtype=int)
rights = np.zeros((h, w), dtype=int)
lefts = np.zeros((h, w), dtype=int)

for i in range(1, h):
    ups[i, :] = (ups[i - 1] + 1) * s[i - 1]

for i in reversed(list(range(h - 1))):
    downs[i, :] = (downs[i + 1] + 1) * s[i + 1]

for i in range(1, w):
    rights[:, i] = (rights[:, i - 1] + 1) * s[:, i - 1]

for i in reversed(list(range(w - 1))):
    lefts[:, i] = (lefts[:, i + 1] + 1) * s[:, i + 1]

ans = (((ups + downs + lefts + rights) * s).max() + 1)
print(ans)


# data_w = []
# data_w_index = []
# data_h = []
# data_h_index = []

# for i in range(h):
#     count = 0
#     index = 0
#     data_w_index_tmp = []
#     data_w_tmp = []
#     for j in range(len(s[i])):
#         # print(s[i][j][0])
#         # print(count)
#         # print(index)
#         if s[i][j] == ".":
#             count += 1
#             data_w_index_tmp.append(index)
#         else:
#             data_w_tmp.append(count)
#             data_w_index_tmp.append(-1)
#             count = 0
#             index += 1
#     data_w_tmp.append(count)
#     # data_w_index_tmp.append(index)

#     data_w_index.append(data_w_index_tmp)
#     data_w.append(data_w_tmp)

# print(data_w)
# print(data_w_index)

# for i in range(w):
#     count = 0
#     index = 0
#     data_h_index_tmp = []
#     data_h_tmp = []
#     for j in range(len(s)):
#         # print(s[i][j][0])
#         # print(count)
#         # print(index)
#         if s[j][i] == ".":
#             count += 1
#             data_h_index_tmp.append(index)
#         else:
#             data_h_tmp.append(count)
#             data_h_index_tmp.append(-1)
#             count = 0
#             index += 1
#     data_h_tmp.append(count)
#     # data_h_index_tmp.append(index)

#     data_h_index.append(data_h_index_tmp)
#     data_h.append(data_h_tmp)

# # print(data_h)
# # print(data_h_index)

# ans = 0
# for i in range(w):
#     for j in range(h):
#         index_h = data_h_index[i][j]
#         index_w = data_w_index[j][i]
#         if index_h != 1:
#             ans_tmp = data_h[i][index_h]+data_w[j][index_w]-1
#             ans = max(ans, ans_tmp)
# print(ans)
