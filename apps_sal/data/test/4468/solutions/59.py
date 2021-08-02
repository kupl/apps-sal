N, S = map(int, input().split())
T = list(map(int, input().split()))
a = S

for n in range(N - 1):
    a += min(S, T[n + 1] - T[n])

print(a)
