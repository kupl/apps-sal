from collections import deque
import sys
import copy

N_MAX = 200000 + 5
INF = 10**9 + 7
sys.setrecursionlimit(N_MAX)
MOD = 10**9 + 7


### BFS ###

nextH = [0, 1, 0, -1]
nextW = [1, 0, -1, 0]


def bfs(u, S):

    S[u[0]][u[1]] = 0  # state を変更

    q = deque()
    q.append(u)
    m = 0
    while q:
        u = q.popleft()
        for h, w in zip(nextH, nextW):
            h += u[0]
            w += u[1]
            if not (0 <= h < len(S) and 0 <= w < len(S[0])):
                continue

            if S[h][w] == '.':  # state を確認
                S[h][w] = S[u[0]][u[1]] + 1  # state を変更
                m = max(m, S[h][w])
                q.append((h, w))
    
    return m


def main():

    H, W = list(map(int, sys.stdin.readline().rstrip().split()))
    S = []
    for _ in range(H):
        S.append([x for x in sys.stdin.readline().rstrip()])

    # print(S)

    m = 0
    for h in range(H):
        for w in range(W):
            D = copy.deepcopy(S)
            if S[h][w] == '.':
                m = max(m, bfs((h, w), D))

    print(m)


main()

