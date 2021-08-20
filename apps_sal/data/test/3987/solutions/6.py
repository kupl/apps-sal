DP = [0] * 4
input()
for x in map(int, input().split()):
    if x == 1:
        DP[0] += 1
        DP[2] += 1
    else:
        DP[1] += 1
        DP[3] += 1
    for j in range(1, 4):
        DP[j] = max(DP[j], DP[j - 1])
print(DP[3])
