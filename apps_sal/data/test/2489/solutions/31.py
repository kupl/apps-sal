def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    M = int(1e6 + 1)
    f = [0] * M
    for x in a:
        if f[x] != 0:
            f[x] += 1
            continue
        for nx in range(x, M, x):
            f[nx] += 1
    ans = 0
    for x in a:
        if f[x] == 1:
            ans += 1
    print(ans)


resolve()
