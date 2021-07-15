N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
ASum, BSum = [0] * (N + 1), [0] * (M + 1)
ASum[0], BSum[0] = A[0], B[0]
AOver, BOver = -1, -1
for i in range(1, N + 1):
    ASum[i] = ASum[i-1] + A[i]
    if AOver == -1 and ASum[i] > K: AOver = i - 1
for i in range(1, M + 1):
    BSum[i] = BSum[i-1] + B[i]
    if BOver == -1 and BSum[i] > K: BOver = i - 1
if AOver == -1: AOver = N
if BOver == -1: BOver = M
ans = 0
import bisect
for i in reversed(range(AOver + 1)):
    if i + BOver <= ans: break
    time = K - ASum[i]
    ans = max(ans, i + bisect.bisect_right(BSum, time) - 1)

print(ans)
