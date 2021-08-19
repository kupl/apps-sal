def main():
    n, x, y = map(int, input().split())
    ans = [0] * (n + 1)
    d = list()
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            # x->yを通らない
            d1 = abs(j - i)
            # i->x->y->jの順 +1はx->yの分
            d2 = abs(x - i) + 1 + abs(j - y)
            # i->y->x->jの順 +1はy->xの分
            d3 = abs(y - i) + 1 + abs(j - x)
            dist = min(min(d1, d2), d3)
            d.append(dist)
            ans[dist] += 1
    print(*ans[1:n], sep='\n')


def __starting_point():
    main()


__starting_point()
