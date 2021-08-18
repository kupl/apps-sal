def solve(N, X):
    layer = [1]
    pate = [1]
    for _ in range(N):
        layer.append(layer[-1] * 2 + 3)
        pate.append(pate[-1] * 2 + 1)

    def burger(n, l):
        if layer[n] <= l:
            return pate[n]
        if l == 0:
            return 0
        re = 0
        if layer[n] // 2 + 1 <= l:
            re += pate[n - 1] + 1
            l -= layer[n] // 2 + 1
        else:
            l -= 1
        re += burger(n - 1, l)
        return re

    print((burger(N, X)))


def __starting_point():
    N, X = list(map(int, input().split()))
    solve(N, X)


__starting_point()
