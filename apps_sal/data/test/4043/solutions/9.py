def main():
    n, d, k = list(map(int, input().split()))
    _min = d + 1

    if n < _min:
        print('NO')
    else:
        res = []
        deg = [0] * (n + 1)
        dist = [0] * (n + 1)

        stack = []
        deg[1] = 1
        for i in range(1, d + 1):
            res.append((i, i + 1))
            if i > 1:
                deg[i] += 2
            dist[i] = max(i - 1, d + 1 - i)
        dist[d + 1] = d
        deg[d + 1] = 1

        for i in range(2, d + 1):
            stack.append(i)

        next = d + 2
        while stack:
            if next > n:
                break
            v = stack.pop()
            if dist[v] < d:
                while next <= n and deg[v] < k:
                    res.append((v, next))
                    deg[v] += 1
                    deg[next] += 1
                    dist[next] = dist[v] + 1
                    if dist[next] < d:
                        stack.append(next)
                    next += 1

        ok = next > n
        ok &= all(deg[i] <= k for i in range(1, n + 1))
        ok &= all(dist[i] <= d for i in range(1, n + 1))

        if not ok:
            print('NO')
        else:
            print('YES')
            for e in res:
                print(*e)


def __starting_point():
    main()


__starting_point()
