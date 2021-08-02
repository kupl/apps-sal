import itertools


def main():
    n, m, r = list(map(int, input().split()))
    rx = [int(i) for i in input().split()]
    inf = 100000000
    wf = [[inf] * n for i in range(n)]
    for i in range(n):
        wf[i][i] = 0

    for i in range(m):
        a, b, c = list(map(int, input().split()))
        wf[a - 1][b - 1] = c
        wf[b - 1][a - 1] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if wf[i][j] > wf[i][k] + wf[k][j]:
                    wf[i][j] = wf[i][k] + wf[k][j]
    cnt = 0
    l = list(itertools.permutations([i for i in range(r)]))
    cnt = inf
    for i in l:
        cnt_sub = 0
        for j in range(r - 1):
            cnt_sub += wf[rx[i[j]] - 1][rx[i[j + 1]] - 1]
        cnt = min(cnt, cnt_sub)
    print(cnt)


main()
