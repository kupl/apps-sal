N = int(input())
A = list(map(int, input().split()))
A.sort()
dp = [0] * (10 ** 5 + 1)
bp = []
for i in range(N):
    if dp[A[i]] != 0:
        bp.append(A[i])
    dp[A[i]] += 1
bp.sort()
p = len(bp)
q = p
o = 0
for i in range(10 ** 5):
    if p < 3:
        break
    p -= 2
if p == 0:
    N -= q
elif p == 1:
    N = N - q - 1
else:
    N = N - q
print(N)
