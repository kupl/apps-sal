import sys

N_MAX = 200000 + 5
INF = 10**9 + 7
sys.setrecursionlimit(N_MAX)
MOD = 10**9 + 7

n = int(input())
Arr = list(map(int,input().split()))

K = 43

#
A = Arr[0]
B = Arr[1]

S = A + B
X = 0
for i in range(2, len(Arr)):
    X ^= Arr[i]

# print(S, X)

# 次を満たすa, b が見つかるか？
#  a+b=S, a^b=X, a<=A

# 桁DP : 桁を一つずつ決めていくようなDP
# dp[今の桁数 = 0:42][繰り上がりがあるか = 0,1][今までがA以下かどうか 0=以下、1=より大きい] = 最大値
# 値は最大値。満たすものがなければ -1
dp = [[[-1 for x in [0, 1]] for _ in [0, 1]] for _ in range(K)]

dp[0][0][0] = 0  # 最初

v = 1
for i in range(K - 1):  # 桁数
    cx = X & 1  # current X
    cs = S & 1  # current S
    ca = A & 1  # current A
    for j in range(2):  # 繰り上がりある／ない
        for k in range(2):  # 今までの範囲が A 以下かどうか
            if dp[i][j][k] == -1:  #
                continue

            for na in range(2):
                for nb in range(2):
                    ni = i + 1
                    nj = 0
                    nk = k
                    if na ^ nb != cx:  # a ^ b = A か？
                        continue

                    ns = na + nb + j
                    if ns % 2 != cs:  # a + b = S か？
                        continue

                    # ここで遷移は確定

                    if ns >= 2:  # 繰り上がり処理
                        nj = 1

                    if ca < na:
                        nk = 1
                    elif ca == na:
                        nk = k
                    else:
                        nk = 0

                    dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] | (v * na))

    X >>= 1
    S >>= 1
    A >>= 1
    v <<= 1
    # print(v)

a = dp[K - 1][0][0]
if a == -1 or a == 0:
    print(-1)
else:
    print(Arr[0] - a)
