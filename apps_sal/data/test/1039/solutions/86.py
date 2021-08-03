def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    node = [0] * N
    for _ in range(N - 1):
        a, b, c = list(map(int, input().split()))
        adj[a - 1].append((b - 1, c))
        adj[b - 1].append((a - 1, c))

    Q, K = list(map(int, input().split()))
    K -= 1

    # import
    from collections import deque

    que = deque([K])
    check = set([K])
    for _ in range(N * 2):
        u = que.popleft()
        for v, c in adj[u]:
            if v in check:
                continue
            node[v] = node[u] + c
            que.append(v)
            check.add(v)
        if len(que) == 0:
            break

    for _ in range(Q):
        x, y = list(map(int, input().split()))
        ans = node[x - 1] + node[y - 1]
        print(ans)


def __starting_point():
    main()


__starting_point()
