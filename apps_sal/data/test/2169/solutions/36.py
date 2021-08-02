import itertools
I = [int(_) for _ in open(0).read().split()]
H, W, D = I[:3]
A = I[3:3 + H * W]
Q = I[3 + H * W]
LR = I[4 + H * W:]

a_i = [0] * (H * W + 1)
for i, a in enumerate(A):
    a_i[a] = i


def calc(a1):
    a2 = a1 + D
    hw1 = a_i[a1]
    h1, w1 = divmod(hw1, W)
    hw2 = a_i[a2]
    h2, w2 = divmod(hw2, W)
    return abs(h2 - h1) + abs(w2 - w1)


score = [0] + [calc(i) for i in range(1, H * W + 1 - D)]
cum = [[0] + list(itertools.accumulate(score[i::D])) for i in range(D)]
ans = []
for l, r in zip(LR[::2], LR[1::2]):
    ans += [cum[r % D][r // D] - cum[l % D][l // D]]
print(*ans, sep='\n')
