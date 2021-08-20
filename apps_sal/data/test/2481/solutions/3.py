import sys
input = sys.stdin.readline


def read():
    (H, W) = list(map(int, input().strip().split()))
    N = 10
    C = []
    for i in range(N):
        c = list(map(int, input().strip().split()))
        C.append(c)
    A = []
    for i in range(H):
        a = list(map(int, input().strip().split()))
        A.append(a)
    return (H, W, N, C, A)


def warshall_floyd(N, G, INF=10 ** 7):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G


def solve(H, W, N, C, A):
    D = warshall_floyd(N, C)
    ans = 0
    for i in range(H):
        for j in range(W):
            a = A[i][j]
            if a >= 0:
                ans += D[a][1]
    return ans


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print('%s' % str(outputs))


__starting_point()
