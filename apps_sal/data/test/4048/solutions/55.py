import math

N = int(input())
N_ = int(math.sqrt(N)) + 1

min_distance = N - 1
for i in range(1, N_):
    p, r = divmod(N, i)
    if r == 0:
        if 1 <= p <= N:
            distance = (i - 1) + (p - 1)
            min_distance = min(min_distance, distance)
        else:
            continue

print(min_distance)
