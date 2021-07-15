import numpy as np
from itertools import product
from collections import  defaultdict as dd
N, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(N)]
wi = wv[0][0]
vi = wv[0][1]
dic = dd(list)
dic_cumsum = dd(list)
for w,v in wv:
    dic[w].append(v)

for k,v in list(dic.items()):
    tmp = sorted(v, reverse=True)
    dic_cumsum[k] = [0] + list(np.zeros((N + 1), dtype=np.int64))
    dic_cumsum[k][1:] = list(np.cumsum(tmp, dtype=np.int64))
for i in range(1,4):
    if wi+i not in list(dic_cumsum.keys()):
        dic_cumsum[wi+i] = [0]
        
n = [len(dic_cumsum[wi]), len(dic_cumsum[wi+1]), len(dic_cumsum[wi+2]), len(dic_cumsum[wi+3])]
m = [list(range(val)) for val in n]
res = 0

for ls in product(m[0], m[1], m[2]):
    if sum(ls)*wi > W:
        continue
    tmp_value = 0
    tmp_weight = 0
    for i,k in enumerate(ls):
        tmp_value += dic_cumsum[wi + i][k]
        tmp_weight += k*(wi+i)
    if tmp_weight > W:
        continue
    # wi, wi+1, wi+2の個数が決まっているので、wi+3を何個取れるかはO(1)で求められる
    max_m3 = (W - tmp_weight) // (wi+3)
    m3 = min(max_m3, n[3]-1)
    tmp_value += dic_cumsum[wi+3][m3]
    if tmp_value > res:
        res = tmp_value
print(res)



