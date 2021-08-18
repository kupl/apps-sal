from collections import deque
import sys
input = sys.stdin.buffer.readline


def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int, input().split())
def MF(): return map(float, input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def TI(): return tuple(map(int, input().split()))


def main():
    n, m = MI()
    G = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = MI()
        G[a].append(b)

    A = [10**5] * (n + 1)

    for i in range(1, n + 1):
        Q = deque([[i, 0]])
        D = [-1] * (n + 1)
        while Q:
            now, d = Q.popleft()
            if now == i and d > 0:
                A[i] = d
                break
            for nx in G[now]:
                if D[nx] == -1:
                    D[nx] = d + 1
                    Q.append([nx, d + 1])

    k = min(A)

    if k == 10**5:
        print(-1)
        return

    s = A.index(k)

    A = []
    Q = deque([[s, 0]])
    D = [10**5] * (n + 1)

    while Q:
        now, d = Q.pop()
        if now == s and d > 0:
            break
        if d == k:
            continue
        A.append(now)
        for nx in G[now]:
            if D[nx] > d + 1:
                D[nx] = d + 1
                Q.append([nx, d + 1])
    D[s] = 0

    ans = []
    d = k - 1
    for i in reversed(A):
        if D[i] == d:
            ans.append(i)
            d -= 1

    print(k)
    print(*ans[::-1], sep="\n")


def __starting_point():
    main()


__starting_point()
