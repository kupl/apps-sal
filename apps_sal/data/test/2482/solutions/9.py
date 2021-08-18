def main():

    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x, y = y, x
            par[x] += par[y]
            par[y] = x
            return True

    def find2(x):
        if pa[x] < 0:
            return x
        else:
            pa[x] = find2(pa[x])
            return pa[x]

    import sys
    input = sys.stdin.readline

    n, k, l = [int(i) for i in input().split()]
    par = [-1] * n
    pa = [-1] * n
    ans = [0] * n

    for i in range(k):
        p, q = [int(i) for i in input().split()]
        unite(p - 1, q - 1)

    def unite2(x, y):
        x = find2(x)
        y = find2(y)
        if x == y:
            return False
        else:
            if pa[x] > pa[y]:
                x, y = y, x
            pa[x] += pa[y]
            pa[y] = x
            return True

    for i in range(l):
        r, s = [int(i) for i in input().split()]
        unite2(r - 1, s - 1)

    dic = {}
    chk = []
    for i in range(n):
        p1 = find(i)
        p2 = find2(i)
        chk.append((p1, p2))
        if (p1, p2) in dic:
            dic[(p1, p2)] += 1
        else:
            dic[(p1, p2)] = 1
    print((' '.join([str(dic[chk[i]]) for i in range(n)])))


def __starting_point():
    main()


__starting_point()
