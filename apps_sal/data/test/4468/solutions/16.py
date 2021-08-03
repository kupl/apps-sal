import sys
input = sys.stdin.readline

N, T = list(map(int, input().split()))
t = list(map(int, input().split()))
t_stop = []
for i in range(N):
    t_stop.append(t[i] + T)
cum_flow = T * N
for i in range(N - 1):
    cum_flow -= max(t_stop[i] - t[i + 1], 0)
print(cum_flow)
