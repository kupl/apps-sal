N = int(input())
Cash = sorted([1] + [6**T for T in range(1, 7)] + [9**T for T in range(1, 6)])
DPList = [0] * (N + 1)
for TN in range(1, N + 1):
    DPList[TN] = min(DPList[TN - TC] + 1 if TN >= TC else 1000000 for TC in Cash)
print(DPList[N])
