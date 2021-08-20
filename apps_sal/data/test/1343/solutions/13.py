try:
    while True:
        (n, m, k) = list(map(int, input().split()))
        edges = [tuple(map(int, input().split())) for i in range(m)]
        if k == 0:
            print(-1)
        else:
            bachery = [False] * n
            for x in map(int, input().split()):
                bachery[x - 1] = True
            result = 10000000000.0
            for (u, v, length) in edges:
                u -= 1
                v -= 1
                if bachery[u]:
                    if not bachery[v]:
                        result = min(result, length)
                elif bachery[v] and (not bachery[u]):
                    result = min(result, length)
            if result > 5000000000.0:
                print(-1)
            else:
                print(result)
except EOFError:
    pass
