N, L = map(int, input().split())
chosen = 1000
for i in range(1, N + 1):
    taste_eaten = L + i - 1
    if abs(taste_eaten) < abs(chosen):
        chosen = taste_eaten
print(int(N * L + N * (N + 1) / 2 - N - chosen))
