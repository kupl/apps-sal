
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


def check(S, i, j):
    if S[i][j] == '
    return '

    num = 0
    for _i in range(max(0, i - 1), min(H, i + 2)):
        for _j in range(max(0, j - 1), min(W, j + 2)):
            if S[_i][_j] == '
            num += 1
    return str(num)


for i in range(H):
    for j in range(W):
        S[i][j] = check(S, i, j)

for i in range(H):
    for j in range(W):
        print(S[i][j], end="")
    print()
