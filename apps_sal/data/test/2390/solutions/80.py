# coding: utf-8

# https://atcoder.jp/contests/abc095/tasks/arc096_b
# 16:55-17:08 chudan
# 12:45-13:08 done


def main():
    N, C = list(map(int, input().split()))
    x = [None] * N
    v = [None] * N
    for i in range(N):
        x[i], v[i] = list(map(int, input().split()))

    cal_clock = [None] * N
    cal = -x[0] + v[0]
    cal_clock[0] = cal if cal > 0 else 0
    for i in range(1, N):
        cal -= x[i] - x[i - 1]
        cal += v[i]
        cal_clock[i] = cal if cal > cal_clock[i - 1] else cal_clock[i - 1]

    cal_anti = [None] * N
    cal = -(C - x[-1]) + v[-1]
    cal_anti[0] = cal if cal > 0 else 0
    for i in range(1, N):
        cal -= x[N - i] - x[N - 1 - i]
        cal += v[N - 1 - i]
        cal_anti[i] = cal if cal > cal_anti[i - 1] else cal_anti[i - 1]

    ans = max(cal_clock[-1], cal_anti[-1])  # 引き返さない場合
    for k in range(N - 1):  # 途中で引き返す場合
        cand_1 = cal_clock[k] - x[k] + cal_anti[N - 2 - k]
        cand_2 = cal_anti[k] - (C - x[N - 1 - k]) + cal_clock[N - 2 - k]
        ans = max(ans, cand_1, cand_2)

    return ans


print((main()))
