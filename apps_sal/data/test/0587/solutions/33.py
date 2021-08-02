def resolve():
    N, K = list(map(int, input().split()))
    TD = sorted([list(map(int, input().split())) for _ in range(N)], reverse=True, key=lambda x: x[1])
    eat_types = set()
    eat_dups = []
    total = 0
    for i in range(K):
        typ, point = TD[i]
        total += point
        if typ in eat_types:
            eat_dups.append(TD[i])
        else:
            eat_types.add(typ)
    ans = total + len(eat_types)**2

    didx = len(eat_dups) - 1
    for i in range(K, N):
        typ, point = TD[i]
        if typ in eat_types:
            continue
        if didx < 0:
            break
        total -= eat_dups[didx][1]
        total += point
        didx -= 1
        eat_types.add(typ)
        ans = max(ans, total + len(eat_types)**2)
    print(ans)


if '__main__' == __name__:
    resolve()
