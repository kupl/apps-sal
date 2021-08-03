def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = list(map(int, input().split()))
    G = [set() for i in range(N)]
    G2 = [set() for i in range(N * 3)]
    for i in range(M):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        G[u].add(v)
    S, T = list(map(int, input().split()))
    S -= 1
    T -= 1

    import collections
    q = collections.deque()
    q.append((S, 0))
    D = [-1] * N * 3
    D[3 * S] = 0
    while(q):
        x, d = q.popleft()
        for y in G[x]:
            if D[y * 3 + (d + 1) % 3] < 0:
                # G2[x*3 + d].add(y)
                q.append((y, d + 1))
                D[y * 3 + (d + 1) % 3] = d + 1

    if D[T * 3] > 0:
        print((D[T * 3] // 3))

    else:
        print((-1))


main()
