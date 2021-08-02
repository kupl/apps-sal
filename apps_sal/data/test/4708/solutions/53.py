N = int(input())    # N泊
K = int(input())    # 最初のK泊までは1泊当たりX円
X = int(input())
Y = int(input())    # K+1泊目以降は1泊当たりY円

if N - K > 0:
    total = (K * X) + ((N - K) * Y)
else:
    total = N * X

print(total)
