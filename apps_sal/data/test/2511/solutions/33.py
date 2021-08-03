from collections import deque
import sys
input = sys.stdin.readline

mod = 10**9 + 7
INF = float("inf")

N, K = list(map(int, input().split()))

edges = [[] * N for _ in range(N)]
for _ in range(N - 1):
    # 頂点の番号を0-indexに直す
    a, b = [int(x) - 1 for x in input().split()]
    edges[a].append(b)
    edges[b].append(a)

# 0をrootとする
dq = deque([0])

# color[i] = i番目の頂点を塗ることが可能な色の数
# visitedの管理も兼ねている（別にvisited配列を作っても特に問題はない）
# 後述するように負の値が入ることを許しているので、-1や0などで初期化するのはNG
color = [INF] * N
color[0] = K

"""
root = 0 から末端に向かって調べる

子1, 子2, 子3, ...と複数の「未着色」の子がある場合、塗ることが出来る色の数は
K-1, K-2, K-3,... (p==0 の場合)
K-2, K-3, K-4,... (p!=0 の場合)　のようになる

子が十分多い場合、どこかで「0」になるので、ans = 0　となる
故に、色の数が負になっても答えには影響しない
"""

while dq:
    # 親となる頂点
    p = dq.popleft()
    # 親をpとした時の、「未着色」な子の数
    cnt = 0
    for c in edges[p]:
        if color[c] == INF:
            if p == 0:
                color[c] = (K - 1 - cnt) % mod
            else:
                color[c] = (K - 2 - cnt) % mod
            cnt += 1
            dq.append(c)

ans = 1
for i in range(N):
    ans = (ans * color[i]) % mod

print(ans)
