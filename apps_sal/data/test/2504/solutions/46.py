from scipy.sparse.csgraph import floyd_warshall

N, M, L = map(int, input().split())
abc = [[int(i) for i in input().split()] for j in range(M)]
Q = int(input())
st = [[int(i) for i in input().split()] for j in range(Q)]
INF = 1 << 30
Path = [[INF for i in range(N)] for j in range(N)]
AnsPath = [[INF for i in range(N)] for j in range(N)]


def PathInit():
    for i in range(N):
        Path[i][i] = 0


PathInit()
for i, j, k in abc:
    Path[i - 1][j - 1] = k
    # 双方向
    Path[j - 1][i - 1] = k

Path = floyd_warshall(Path)

for i in range(N):
    for j in range(N):
        if Path[i][j] <= L:
            AnsPath[i][j] = 1
AnsPath = floyd_warshall(AnsPath)
for s, t in st:
    if AnsPath[s - 1][t - 1] == INF:
        print(-1)
    else:
        print(int(AnsPath[s - 1][t - 1] - 1))
