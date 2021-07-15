import sys
Q = int(input())
for _ in range(Q):
    N, M = map(int, sys.stdin.readline().split())
    G = [[1 if s == '*' else 0 for s in sys.stdin.readline().strip()] for _ in range(N)]
    ans = 10**9+7
    G1 = [sum(g) for g in G]
    G = list(map(list, zip(*G)))
    G2 = [sum(g) for g in G]
    G = list(map(list, zip(*G)))
    K = N + M - 1
    for i in range(N):
        for j in range(M):
            if G[i][j]:
                ans = min(ans, K - (G1[i] + G2[j] - 1))
            else:
                ans = min(ans, K - (G1[i] + G2[j]))
    sys.stdout.write('{}\n'.format(ans))
