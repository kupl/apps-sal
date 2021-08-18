from itertools import accumulate
import sys
input = sys.stdin.readline

S = input().strip()
mod = 10**9 + 7
LEN = len(S)

ANS = [0] * (LEN + 1)
ANS2 = [0] * (LEN + 1)
ANS3 = [0] * (LEN + 1)

for i in range(LEN):
    x = int(S[LEN - 1 - i])

    k = LEN - i - 1
    p = k * (k + 1) // 2
    ANS[i] += x * p

    ANS2[0] += x
    ANS2[i] -= x
    ANS3[i] -= i * x

ANS2 = list(accumulate(ANS2))
for i in range(LEN + 1):
    ANS2[i] += ANS3[i]
ANS2 = list(accumulate(ANS2))


A = 0
for i in range(LEN):
    A += (ANS[i] + ANS2[i]) * pow(10, i, mod)
    A %= mod

print(A)
