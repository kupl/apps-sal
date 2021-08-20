def HonestOrUnkind2():
    n = int(input())
    lang = [[-1] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        a = int(input())
        for _ in range(a):
            (x, y) = list(map(int, input().split()))
            lang[i][x - 1] = y
    for i in range(2 ** n):
        status = [0 for _ in range(n)]
        for j in range(n):
            if i >> j & 1:
                status[j] = 1
        ans0 = True
        for j in range(n):
            if status[j] == 1:
                for k in range(n):
                    if lang[j][k] == -1:
                        continue
                    if lang[j][k] != status[k]:
                        ans0 = False
        if ans0:
            ans = max(ans, status.count(1))
    print(ans)


def __starting_point():
    HonestOrUnkind2()


__starting_point()
