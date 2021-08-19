N = int(input())
S = input()
EP = [0] * (N + 1)
WP = [0] * (N + 1)
CP = [0] * N
for T in range(0, N):
    EP[N - T - 1] = EP[N - T] + (S[N - 1 - T] == 'E')
    WP[T + 1] = WP[T] + (S[T] == 'W')
for T in range(0, N):
    CP[T] = EP[T + 1] + WP[T]
print(min(CP))
