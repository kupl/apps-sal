import numpy as np

N = int(input())
t = np.array(['0'] + input().split(), np.int64)
v = list(map(int, input().split()))


T = np.cumsum(t).tolist()
arrival = T[-1]
times = np.arange(0, arrival + 0.5, 0.5)
speed_limit = np.minimum(times, times[::-1])

for i, j, k in zip(T, T[1:], v):
    speed1 = i - times + k
    speed2 = np.full(arrival * 2 + 1, k, np.float)
    speed3 = times - j + k

    speed = np.maximum(speed1, speed3)
    speed = np.maximum(speed2, speed)
    speed_limit = np.minimum(speed_limit, speed)

answer = np.abs(speed_limit[1:] + speed_limit[:-1]) * 0.5 / 2
print((answer.sum()))
