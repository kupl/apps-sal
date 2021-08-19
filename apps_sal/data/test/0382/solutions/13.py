3


def calc(l, r, layers, li):
    if r - l == 1:
        return layers[li][l]
    xl = l
    if l % 2 == 1:
        xl -= 1
    xr = r
    if r % 2 == 1:
        xr += 1
    ans = calc(xl // 2, xr // 2, layers, li + 1)
    if xl != l:
        ans -= layers[li][xl]
    if xr != r:
        ans -= layers[li][xr - 1]
    return ans


def solve(N, M, Q, S, T, A):
    base = [0] * N
    i = 0
    while True:
        try:
            i = S.index(T, i)
            base[i] = 1
            i += 1
        except ValueError:
            break
    layers = [base]
    while len(layers[-1]) > 1:
        prev = layers[-1]
        if len(prev) % 2 == 1:
            prev.append(0)
        layer = []
        for i in range(len(prev) // 2):
            layer.append(prev[2 * i] + prev[2 * i + 1])
        layers.append(layer)
    ans = []
    for (l, r) in A:
        l -= 1
        r -= M - 1
        if r <= l:
            ans.append(0)
            continue
        ans.append(calc(l, r, layers, 0))
    return ans


def main():
    (N, M, Q) = [int(e) for e in input().split(' ')]
    S = input()
    T = input()
    A = [map(int, input().split(' ')) for _ in range(Q)]
    assert len(S) == N
    assert len(T) == M
    print(*solve(N, M, Q, S, T, A), sep='\n')


def __starting_point():
    main()


__starting_point()
