from collections import deque
import sys
sys.setrecursionlimit(10**9)
def read(): return sys.stdin.readline()


def read_ints():
    return list(map(int, read().split()))


def read_intgrid(h):
    return list(list(map(int, read().split()))for i in range(h))


def main():
    # input data
    n, m = read_ints()
    A = read_ints()
    B = read_ints()
    G = [[] for _ in range(n)]
    for i in range(m):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        G[c].append(d)
        G[d].append(c)

    # solve
    ans = 1
    vis = [0] * n

    def bfs(v):
        queue = deque([v])
        vis[v] = 1
        tmp1 = A[v]
        tmp2 = B[v]
        while queue:
            x = queue.popleft()
            for y in G[x]:
                if vis[y]:
                    continue
                tmp1 += A[y]
                tmp2 += B[y]
                vis[y] = 1
                queue.append(y)
        # print(v,tmp1,tmp2)
        if tmp1 == tmp2:
            return True
        else:
            return False

    for i in range(n):
        if vis[i]:
            continue
        if not bfs(i):
            ans = 0
            break

    return print('Yes' if ans else 'No')


def __starting_point():
    main()


__starting_point()
