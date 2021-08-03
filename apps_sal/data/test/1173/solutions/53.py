def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in [0] * n]
    m = (n * (n - 1)) // 2
    d = dict()
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            d[(i, j)] = cnt
            cnt += 1
    g = [[] for _ in [0] * m]
    gr = [0] * m
    for i in range(n):
        temp = []
        for j in a[i]:
            if i >= j:
                temp.append(d[(j - 1, i)])
            else:
                temp.append(d[(i, j - 1)])
        for j, k in enumerate(temp[1:]):
            g[temp[j]].append(k)
            gr[k] += 1
    q = [i for i, j in enumerate(gr) if j == 0]
    cnt = 0
    while q:
        cnt += 1
        qq = []
        for i in q:
            for j in g[i]:
                gr[j] -= 1
                if gr[j] == 0:
                    qq.append(j)
        q = qq
    if sum(gr) == 0:
        print(cnt)
    else:
        print(-1)


main()
