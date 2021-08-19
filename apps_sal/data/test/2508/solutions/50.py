import sys
import collections
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def main():
    (H, W, K) = [int(x) for x in input().split()]
    (X1, Y1, X2, Y2) = [int(x) for x in input().split()]
    C = [input().strip() for _ in range(H)]
    q = collections.deque()
    q.append((X1 - 1, Y1 - 1, 0))
    V = [[float('inf')] * W for j in range(H)]
    V[X1 - 1][Y1 - 1] = 0
    while q:
        c = q.popleft()
        x = c[0]
        y = c[1]
        d = c[2]
        if y == Y2 - 1 and x == X2 - 1:
            print(c[2])
            return
        (e, w, n, s) = (True, True, True, True)
        for k in range(1, K + 1):
            if not e and (not w) and (not n) and (not s):
                break
            if e:
                if y + k >= W or C[x][y + k] == '@':
                    e = False
                else:
                    if V[x][y + k] == float('inf'):
                        V[x][y + k] = d + 1
                        q.append((x, y + k, d + 1))
                    if V[x][y + k] < d + 1:
                        e = False
            if w:
                if y - k < 0 or C[x][y - k] == '@':
                    w = False
                else:
                    if V[x][y - k] == float('inf'):
                        V[x][y - k] = d + 1
                        q.append((x, y - k, d + 1))
                    if V[x][y - k] < d + 1:
                        w = False
            if n:
                if x - k < 0 or C[x - k][y] == '@':
                    n = False
                else:
                    if V[x - k][y] == float('inf'):
                        V[x - k][y] = d + 1
                        q.append((x - k, y, d + 1))
                    if V[x - k][y] < d + 1:
                        n = False
            if s:
                if x + k >= H or C[x + k][y] == '@':
                    s = False
                else:
                    if V[x + k][y] == float('inf'):
                        V[x + k][y] = d + 1
                        q.append((x + k, y, d + 1))
                    if V[x + k][y] < d + 1:
                        s = False
    print(-1)


def __starting_point():
    main()


__starting_point()
