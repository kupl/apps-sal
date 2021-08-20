def solve():
    (H, W) = list(map(int, input().split()))
    S = [input() for i in range(H)]
    for i in range(H):
        S[i] = list(S[i])
    for i in range(H):
        for k in range(W):
            if S[i][k] != '#':
                c = 0
                if i > 0 and k > 0 and (S[i - 1][k - 1] == '#'):
                    c += 1
                if i > 0 and S[i - 1][k] == '#':
                    c += 1
                if i > 0 and k < W - 1 and (S[i - 1][k + 1] == '#'):
                    c += 1
                if k > 0 and S[i][k - 1] == '#':
                    c += 1
                if k < W - 1 and S[i][k + 1] == '#':
                    c += 1
                if i < H - 1 and k > 0 and (S[i + 1][k - 1] == '#'):
                    c += 1
                if i < H - 1 and S[i + 1][k] == '#':
                    c += 1
                if i < H - 1 and k < W - 1 and (S[i + 1][k + 1] == '#'):
                    c += 1
                S[i][k] = str(c)
    for i in range(H):
        print(''.join(S[i]))


def __starting_point():
    solve()


__starting_point()
