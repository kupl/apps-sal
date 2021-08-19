from itertools import accumulate
MOD = 10 ** 9 + 7
(N, K) = list(map(int, input().split()))


def N2sqrtN(N):
    M = int(N ** 0.5)
    As = list(range(1, M + 1))
    Bs = [N // A for A in reversed(As)]
    if As[-1] == Bs[0]:
        return As + Bs[1:]
    else:
        return As + Bs


Bs = N2sqrtN(N)
lenB = len(Bs)
nums = [1]
for i in range(lenB - 1):
    nums.append(Bs[i + 1] - Bs[i])
dp = [0] * lenB
dp[0] = 1
for i in range(1, K + 1):
    dp = list(accumulate(dp))
    dp = [dpi * num % MOD for (dpi, num) in zip(reversed(dp), nums)]
print(sum(dp) % MOD)
