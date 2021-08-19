import sys
sys.setrecursionlimit(10**9)  # 再帰の上限指定
# 木構造の標準入力
N, Q = list(map(int, input().split()))
T = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    T[a].append(b)
    T[b].append(a)

# 入力例1のとき、繋がる頂点のリスト [[1], [0, 2, 3], [1], [1]]
# 足算部分の標準入力
V = [0] * N
for _ in range(Q):
    p, x = list(map(int, input().split()))
    V[p - 1] += x
# 入力例1のとき、各ノード以下に足す値 [100, 10, 1, 0]


def dfs(now, prev=-1):
    for next in T[now]:
        if next != prev:  # 親じゃなければ、(子であれば)足し算する
            V[next] += V[now]
            dfs(next, now)


dfs(0)
"""
入力例1のとき
dfs(0,-1)→dfs(1,0)→dfs(2,1)
                  →dfs(3,1)
"""
print((*V))
