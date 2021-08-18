N, T = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]

T_start = 0
T_end = T
T_total = 0

for i in range(1, N):
    if t[i] <= T_end:
        T_end = t[i] + T
    else:
        T_total += T_end - T_start
        T_start = t[i]
        T_end = t[i] + T

T_total += T_end - T_start

print(T_total)
