def f(G, not_searched, results={0: '0'}):
    stack = []
    while len(not_searched) > 0:
        if len(stack) > 0:
            i = stack.pop()
            not_searched.remove(i)
        else:
            i = not_searched.pop()

        for key, val in G[i].items():
            if not key in not_searched:
                continue

            if val % 2 == 1:
                if results[i] == '0':
                    results[key] = '1'
                else:
                    results[key] = '0'
            else:
                results[key] = results[i]

            stack.append(key)

    return results


N = int(input())
G = [{} for _ in range(N)]
not_searched = set([i for i in range(N)])

if N == 1:
    print(results[0])
else:
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1][v - 1] = w
        G[v - 1][u - 1] = w

    results = f(G, not_searched)
    for i in range(N):
        print(results[i])
