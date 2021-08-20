from bisect import bisect_left, bisect_right
N = int(input())
seq = [0] * N
for i in range(N):
    seq[i] = -1 * int(input())
'\n#リストseqからLISの長さを出す\nLIS = [seq[0]]\nfor i in range(len(seq)):\n    if seq[i] >= LIS[-1]:\n        LIS.append(seq[i])\n    else:\n        LIS[bisect_right(LIS, seq[i])] = seq[i]\n\nprint(len(LIS) - 1)\n#print(LIS)\n'


def getLIS(_N, a):
    INF = 1e+18
    MaxP = _N + 10
    dp = [INF for _ in range(MaxP)]
    for i in range(_N):
        dp[bisect_right(dp, a[i])] = a[i]
    return dp[:bisect_left(dp, INF)]


LIS2 = getLIS(N, seq)
print(len(LIS2))
