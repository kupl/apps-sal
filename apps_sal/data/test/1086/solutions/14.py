def ints():
    return [int(x) for x in input().split()]


def readi():
    return int(input())


(H, W) = ints()
A = [ints() for _ in range(H)]
B = [ints() for _ in range(H)]
D = [[abs(A[h][w] - B[h][w]) for w in range(W)] for h in range(H)]
memo = {}
memo = {}
N = 80 * 60
memo[0, 0] = 1 << D[0][0] + N
for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            continue
        d = D[h][w]
        f = 0
        if h > 0:
            s = memo[h - 1, w]
            f |= s << d
            f |= s >> d
        if w > 0:
            s = memo[h, w - 1]
            f |= s << d
            f |= s >> d
        memo[h, w] = f


def min_keta(n):
    b = bin(n >> N)
    for i in range(len(b)):
        if b[-i - 1] == '1':
            return i


print(min_keta(memo[H - 1, W - 1]))
