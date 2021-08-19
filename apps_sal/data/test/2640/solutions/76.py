import numpy as np
(h, w) = map(int, input().split())
S = list((list(input()) for _ in range(h)))
S = np.array(S)
S_int = np.zeros_like(S, dtype=int)
S_int[S == '.'] = 1


def getLR(d, width, height):
    L = np.zeros_like(d)
    R = L.copy()
    L[:][0] = 0
    R[:][-1] = 0
    for i in range(1, width):
        ridx = width - 1 - i
        L[:, i] = d[:, i] * (L[:, i - 1] + d[:, i - 1])
        R[:, ridx] = d[:, ridx] * (R[:, ridx + 1] + d[:, ridx + 1])
    return (L, R)


(L, R) = getLR(S_int, w, h)
(U, D) = getLR(S_int.T, h, w)
print((L + R + U.T + D.T).max() + 1)
