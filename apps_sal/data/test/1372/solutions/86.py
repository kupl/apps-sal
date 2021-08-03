H, N = map(int, input().split())

magic = [tuple(map(int, input().split())) for _ in range(N)]

DP = [0] * (H + 10**4)

for h in range(1, H + 1):
    DP[h] = min(DP[h - damage] + mp for damage, mp in magic)
print(DP[H])
