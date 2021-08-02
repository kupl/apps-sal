import itertools
import copy

H, W, K = list(map(int, input().split()))
c = [list(str(input())) for i in range(H)]
ans = 0
H_bit = list(itertools.product([0, 1], repeat=H))
W_bit = list(itertools.product([0, 1], repeat=W))


def mark(h, w, board):
    for i, n in enumerate(h):
        if n == 1:
            board[i] = ["R"] * W
    for j, n in enumerate(w):
        if n == 1:
            for k in range(H):
                board[k][j] = 'R'
    return board


for i in H_bit:
    for j in W_bit:
        check = copy.deepcopy(c)
        li = mark(i, j, check)
        if sum(a.count("#") for a in li) == K:
            ans += 1
print(ans)
