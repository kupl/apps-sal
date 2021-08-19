from collections import deque
import sys
input = sys.stdin.readline
mod = 10 ** 9 + 7
INF = float('inf')
(N, K) = list(map(int, input().split()))
edges = [[] * N for _ in range(N)]
for _ in range(N - 1):
    (a, b) = [int(x) - 1 for x in input().split()]
    edges[a].append(b)
    edges[b].append(a)
dq = deque([0])
color = [INF] * N
color[0] = K
'\nroot = 0 から末端に向かって調べる\n\n子1, 子2, 子3, ...と複数の「未着色」の子がある場合、塗ることが出来る色の数は\nK-1, K-2, K-3,... (p==0 の場合)\nK-2, K-3, K-4,... (p!=0 の場合)\u3000のようになる\n\n子が十分多い場合、どこかで「0」になるので、ans = 0\u3000となる\n故に、色の数が負になっても答えには影響しない\n'
while dq:
    p = dq.popleft()
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
    ans = ans * color[i] % mod
print(ans)
