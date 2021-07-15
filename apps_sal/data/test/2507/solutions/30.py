# # もし修行により消化コストが全て0になる場合
# if sum(a_list) <= k:
#     print(0)
#     return

# # 更新メソッド
# def update_cost(max_idx, result_cost, a_list, f_list):

#     result_cost[max_idx] = a_list[max_idx] * f_list[max_idx]

#     if max_idx == 0:
#         pass
#     else:
#         result_cost[max_idx-1] = a_list[max_idx-1] * f_list[max_idx-1]

#     return result_cost

# # ソート
# a_list.sort()
# f_list.sort(reverse=True)

# # コストリストinit
# result_cost = [a_list[idx] * f_list[idx] for idx in range(len(a_list))]


# # 修行する
# while k > 0:
#     # 現状で最もコストが大きいものについて考える
#     max_idx = result_cost.index(max(result_cost))

#     # 修行実行
#     a_list[max_idx] -= 1
#     a_list.sort()

#     # コストリスト更新
#     result_cost = update_cost(max_idx, result_cost, a_list, f_list)

#     # 修行数減らす
#     k -= 1

# print(max(result_cost))

import numpy as np
n, k = list(map(int, input().split()))

A = np.array(input().split(), np.int)
F = np.array(input().split(), np.int)

A.sort()
F.sort()
F = F[::-1]

left = -1 
right = (A * F).sum()

while (right-left) > 1:
    # print(left, right)
    split_line = (left + right) // 2
    r = np.maximum(0, A-split_line // F).sum() <= k
    if r:
        right = split_line
    else:
        left = split_line

print(right)


