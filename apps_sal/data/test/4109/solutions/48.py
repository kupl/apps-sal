def main():
    (n, m, x) = list(map(int, input().split()))
    sofar = 10 ** 5 + 1
    cl = list((list(map(int, input().split())) for _ in range(n)))
    ans = float('inf')
    for i in range(2 ** n):
        tmp = [0] * m
        cost = 0
        for j in range(n):
            if i >> j & 1:
                for k in range(m):
                    tmp[k] += cl[j][k + 1]
                cost += cl[j][0]
        for t in tmp:
            if t < x:
                break
        else:
            ans = min(ans, cost)
    if ans == float('inf'):
        return -1
    else:
        return ans


def __starting_point():
    print(main())


__starting_point()
