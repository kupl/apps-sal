N = int(input())
S = list(input())
dp_f = [0 for _ in range(N)]
dp_b = [0 for _ in range(N)]
for n in range(1, N):
    if S[n - 1] == 'W':
        tmp = 1
    else:
        tmp = 0
    dp_f[n] = dp_f[n - 1] + tmp
for n in reversed(range(N - 1)):
    if S[n + 1] == 'E':
        tmp = 1
    else:
        tmp = 0
    dp_b[n] = dp_b[n + 1] + tmp
MIN = N
for n in range(N):
    if n == N - 1:
        MIN = min(MIN, dp_f[N - 1])
    elif n == 0:
        MIN = min(MIN, dp_b[0])
    else:
        MIN = min(MIN, dp_f[n] + dp_b[n])
print(MIN)
