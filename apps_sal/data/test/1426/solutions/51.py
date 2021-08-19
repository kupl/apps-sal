from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines


def main():
    lines = input()
    n, m = list(map(int, lines[0].split()))
    # 隣接リスト
    edges = [[] for i in range(n)]
    for i in range(m):
        u, v = list(map(int, lines[i + 1].split()))
        edges[u - 1].append(v - 1)

    s, t = list(map(int, lines[m + 1].split()))
    inf = 100000000000
    score = [[inf] * 3 for i in range(n)]
    now = deque()
    now.append((s - 1, 0))
    score[s - 1][0] = 0

    def bfs():
        if now:
            u, mod = now.popleft()
            time = score[u][mod]
            mod = (mod + 1) % 3
            for v in edges[u]:
                if score[v][mod] == inf:
                    score[v][mod] = time + 1
                    now.append((v, mod))

            bfs()

    bfs()
    ans = score[t - 1][0]
    if ans == inf:
        print(-1)
    else:
        print(score[t - 1][0] // 3)


main()
