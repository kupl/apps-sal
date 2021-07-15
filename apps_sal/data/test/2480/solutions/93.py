import sys
import numpy as np
from collections import defaultdict

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
A = np.array([1] + lr())
A = (A-1) % K
N += 1
# 累積和が同じになっている箇所に注目、要素がK-1離れている組み合わせは無理
Acum = (A.cumsum() % K).tolist()
answer = 0
dic = defaultdict(int)
for i, cur in enumerate(Acum): 
    answer += dic[cur]
    dic[cur] += 1
    if i >= K-1:
        vanish = Acum[i-(K-1)]
        dic[vanish] -= 1

print(answer)
# 10

