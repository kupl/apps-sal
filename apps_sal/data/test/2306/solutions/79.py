import numpy as np

N = int(input())
t = np.array(['0'] + input().split(), np.int64)
v = list(map(int, input().split()))

# 発車してからn秒後の速度を求める

T = np.cumsum(t).reshape(-1, 1)
arrival = T[-1]
times = np.arange(0, arrival + 0.5, 0.5)
speed_limit = np.minimum(times, times[::-1])

V = np.array(v).reshape(-1, 1)
answer = np.minimum(times, times[::-1])
tmp = np.maximum(T[:-1, :] - times, times - T[1:, :]) + V
tmp = np.maximum(tmp, V)
tmp = tmp.min(axis=0)
answer = np.minimum(tmp, answer)
answer = np.abs(answer[1:] + answer[:-1]) * 0.5 / 2

print((answer.sum()))

