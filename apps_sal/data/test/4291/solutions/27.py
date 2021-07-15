import numpy as np

N, Q = map(int, input().split())
S = input()

X = np.zeros(N+1, dtype='int64')
tmp = 1 # いま何文字目か
while S.find('AC') >= 0 and tmp < N:
    i = S.find('AC')
    X[tmp+i] += 1 # AC の A がある場所に 1 を加算
    S = S[i+2:] # 2文字進める
    tmp += i + 2
SUM = X.cumsum()

for _ in range(Q):
    l, r = map(int, input().split())
    # A の右隣の C まで含まれていないといけないので、
    # r文字目ではなく、r-1文字目までで考える
    print(SUM[r-1] - SUM[l-1])
