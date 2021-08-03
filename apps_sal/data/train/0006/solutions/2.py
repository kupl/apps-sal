import sys

T = int(sys.stdin.readline().strip())
for t in range(0, T):
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    P = [[] for i in range(0, n)]
    G = [0] * n
    for i in range(0, m):
        x, y = list(map(int, sys.stdin.readline().strip().split()))
        x, y = x - 1, y - 1
        P[y].append(x)
    ans = []
    for i in range(0, n):
        for j in P[i]:
            for k in P[j]:
                if G[j] == 0 and G[k] == 0:
                    if G[i] == 0:
                        ans.append(str(i + 1))
                        G[i] = 1

    print(len(ans))
    print(" ".join(ans))
