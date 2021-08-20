N = list(map(int, input()))
ans = 0
DP = [0] * 2
DP[0] = 0
DP[1] = 1
for i in N:
    (a, b) = (DP[0], DP[1])
    DP[0] = a + i if a + i < b + (10 - i) else b + (10 - i)
    DP[1] = a + i + 1 if a + i + 1 < b + (9 - i) else b + (9 - i)
print(DP[0] if DP[0] <= DP[1] + 1 else DP[1] + 1)
