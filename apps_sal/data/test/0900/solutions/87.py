import numpy as np
import sys


def input():
    return sys.stdin.readline()[:-1]

# S = [int(x) if x!="?" else -1 for x in input()]

# print (S)

# div_num = 1000000007
# arr = np.arange(13, dtype = np.uint64)
# # dp = np.zeros([2, 13], dtype = np.uint64)

# div13_list = [1]
# for ii in range(1, len(S)):
#     n = div13_list[-1] * 10 % 13
#     if n in div13_list:
#         break
#     else:
#         div13_list.append(n)
# div13_mat = np.array([div13_list] * 10, dtype = int)
# div13_mat = (div13_mat * np.arange(10)[:, None] % 13).T

# if S[-1] == -1:
#     dp[0, :10] = 1
# else:
#     dp[0, S[-1]] = 1

# for ii in range(1, len(S)):
#     # ind = -ii-1
#     # tmp = div13_mat[ii%6]
#     # if S[ind] == -1:
#     #     for n in range(10):
#     #         res = np.roll(arr, -tmp[n])
#     #         # dp[1, res] += dp[0, arr]
#     # else:
#     #     res = np.roll(arr, -tmp[S[ind]])
#     #     # dp[1, res] += dp[0, arr]
#     dp[0] = dp[1] % div_num
#     dp[1] = 0


# print (dp[0, 5])

#
# 大きい方の桁からやってく方法
#

MOD = 1000000007

S = [int(x) if x != "?" else -1 for x in input()]
n = len(S)

# r[i]
# 現在考えてる一つ前の桁数で、余りが i になる整数の個数
r = [0] * 13

# まず一つ目の値が１の位とする
s = S[0]
if (s != -1):
    r[s] = 1
else:
    for i in range(10):
        r[i] = 1

# 桁を進めながら個数をカウント
for i in range(1, n):
    # dp[j]
    # 現在考えている桁(i)を除く、余りが j となる整数の個数
    dp = [0] * 26

    # 桁が一つ上がるので、一つ前の余りが 10 倍になる
    for j in range(13):
        dp[j * 10 % 13] += r[j] % MOD

    # アクセスを高速にするため２倍の長さとる (dp[i] == dp[i + 13])
    dp[13:26] = dp[0:13]

    r = [0] * 13

    s = S[i]
    if (s == -1):
        w = sum(dp[4:14])
        for j in range(13):
            r[j] += w
            w += dp[j + 1] - dp[j + 4]
    else:
        for j in range(13):
            r[j] += dp[13 - s + j]
print((r[5] % MOD))
