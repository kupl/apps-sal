from bisect import bisect_left, bisect_right
N = int(input())
seq = [0] * N
for i in range(N):
  seq[i] = (-1) * int(input())

"""
#リストseqからLISの長さを出す
LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] >= LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect_right(LIS, seq[i])] = seq[i]

print(len(LIS) - 1)
#print(LIS)
"""
def getLIS(_N,a):
  INF = 1e18
  MaxP = _N+10
  dp = [INF for _ in range(MaxP)]
  for i in range(_N):
    dp[bisect_right(dp,a[i])] = a[i]

  #print(dp[:10])
  return dp[:bisect_left(dp, INF)]

LIS2 = getLIS(N,seq)

print(len(LIS2))
