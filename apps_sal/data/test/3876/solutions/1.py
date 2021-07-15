import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import numpy as np

MOD = 10 ** 9 + 7
N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x,y = list(map(int,input().split()))
    graph[x].append(y)
    graph[y].append(x)

"""
包除の原理。各頂点を根として
・偶数個を選ぶ、そこが反例となっている、他は何でもよい、
・奇数個を選ぶ、そこが反例となっている、他は何でもよい
・根を含む成分は保留してある。保留している頂点の数を持っておく。
・偶数個の場合と奇数の場合の差分だけ持っておく
"""

def dp_merge(data1,data2):
    N1 = len(data1) - 1
    N2 = len(data2) - 1
    if N1 > N2:
        N1,N2 = N2,N1
        data1,data2 = data2,data1
    data = np.zeros(N1+N2, dtype = np.int64)
    for n in range(1,N1+1):
        data[n:n+N2] += data1[n] * data2[1:] % MOD
    data %= MOD
    return data

fact_2 = [1,0,1]
for n in range(3,N+10):
    fact_2.append(fact_2[n-2] * (n-1) % MOD)
fact_2 = np.array(fact_2, dtype = np.int64)

def dp_add_edge(data):
    N = len(data) - 1
    data1 = np.zeros(N+2, dtype=np.int64)
    # 辺を反例に加えない
    data1[1:] = data
    # 辺を反例に加える
    data1[1] = - (data * fact_2[:N+1] % MOD).sum() % MOD
    return data1

def dfs(v, parent = None):
    data = None
    for y in graph[v]:
        if y == parent:
            continue
        data1 = dfs(y, v)
        # mergeする前に、最後の辺をひとつ加える
        data1 = dp_add_edge(data1)
        if data is None:
            data = data1
        else:
            data = dp_merge(data, data1)
    if data is None:
        return np.array([0,1],dtype=np.int64)
    return data

data = dfs(1)

answer = (data * fact_2[:N+1] % MOD).sum() % MOD

print(answer)


