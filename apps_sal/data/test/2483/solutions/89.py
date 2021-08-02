import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, c = list(map(int, input().split()))
    STC = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: [x[2], x[0]])

    STC2 = []
    tmp = STC[0]
    for i in range(1, n):
        pre_s, pre_t, pre_c = tmp
        now_s, now_t, now_c = STC[i]
        if pre_c == now_c:
            if pre_t == now_s:
                tmp = [pre_s, now_t, now_c]
            else:
                STC2.append(tmp)
                tmp = STC[i]
        else:
            STC2.append(tmp)
            tmp = STC[i]
    if len(tmp):
        STC2.append(tmp)

    imos = [[0] * (10 ** 5 + 1) for _ in range(c)]
    for i in range(len(STC2)):
        s, t, c = STC2[i]
        imos[c - 1][s - 1] += 1
        imos[c - 1][t] -= 1

    for i in range(c):
        for j in range(1, 10 ** 5 + 1):
            imos[i][j] += imos[i][j - 1]

    res = [0] * (10 ** 5 + 1)
    for i in range(c):
        for j in range(10 ** 5 + 1):
            res[j] += imos[i][j]

    print((max(res)))


def __starting_point():
    resolve()


__starting_point()
