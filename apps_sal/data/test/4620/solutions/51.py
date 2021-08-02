import numpy as np
N = int(input())
C, S, F = [], [], []
for _ in range(N - 1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)
S.append(0)


def theta(x):  # ヘヴィサイドの段差関数
    return x if x > 0 else 0


def DptTimeAtNextSt(i, T):  # 時刻Tに駅iを出発した時、駅i+1を出発する時間
    nonlocal C, S, F
    arrT = T + C[i]
    if i == N - 2: return arrT
    return S[i + 1] + np.ceil(theta(arrT - S[i + 1]) / F[i + 1]) * F[i + 1]


def solve(i, S):  # 駅iに対する解を再帰的に解く関数
    if i == N - 1:
        return int(S)
    else:
        return solve(i + 1, DptTimeAtNextSt(i, S))


for i in range(N):
    print(solve(i, S[i]))
