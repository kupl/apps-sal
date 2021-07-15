#解説方針#解法1
#https://qiita.com/ZhangChaoran/items/71fab0e4b8647a93d3a0
from collections import deque
from heapq import heappop, heappush
#標準入力
N = int(input())
MOD = 10 ** 9 + 7
L = [[] for i in range(N + 1)] #dfs用
for i in range(N - 1):
  a, b = map(int, input().split())
  L[a].append(b)
  L[b].append(a)

#木の探索
parent = [0] * (N + 1)
order = []
stack = [1]
while stack:
    x = stack.pop()
    order.append(x)  # 行きがけ順探索リスト
    for y in L[x]:
        if y == parent[x]:
            continue
        parent[y] = x  # 親ノードを記録
        stack.append(y)
#print(order, parent)

half = pow(2, MOD - 2, MOD)
power_inv = [1] * (N + 1)#2 ** N の逆元の集合
size = [1] * (N + 1)
for i, v in enumerate(order[::-1], 1):#iが1から
    p = parent[v]
    x = size[v]  # vの子孫ノード数（自分も含む）をとる
    size[p] += x  # 親にノード数を加算
    power_inv[i] = power_inv[i - 1] * half % MOD  # [1, 1/2, 1/4, ...]
#print(size)
# 辺iがSに含まれるための必要十分条件による辺の個数の期待値 
# (1 - (1/2) ** i)(1 - (1/2) ** (N - i))を展開して計算
# 根である1の頂点以外は、ある頂点とその親を結ぶ辺を考えた際
# i と N - i個の頂点に別れるので,size[2:]でOK
ans = sum((1 - power_inv[i] - power_inv[N - i] + power_inv[N]) %
          MOD for i in size[2:])  
#ans = sum((1 - (1/2) ** i- (1/2) ** (N - i) + (1/2) ** N) for i in size[2:])  
#print(ans)
ans += 1  # 木の頂点の個数は辺の個数+1
# -「すべての辺が含まれない、つまり空グラフの場合の誤加算」-N/2
ans -= power_inv[N] + N * power_inv[1]  
#ans -= N * power_inv[1]  
ans %= MOD

print(ans)
