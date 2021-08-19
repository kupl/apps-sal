# 最初のK泊までは、1泊あたりX円
# K+1泊目以降は、1泊あたりY円
# N泊したときの宿泊費

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    print(X * N)
else:
    print(X * K + Y * (N - K))
