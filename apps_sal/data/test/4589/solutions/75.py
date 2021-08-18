import itertools
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for x, y in itertools.product(range(W), range(H)):
    if S[y][x] == ".":
        res = 0
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if 0 <= x + i and x + i < W and 0 <= y + j and y + j < H:
                if S[y + j][x + i] == "
                res += 1

        S[y][x] = res

for j in range(H):
    L = [str(a) for a in S[j]]
    print(''.join(L))
