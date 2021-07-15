import numpy as np


def main():
    H, W, K = list(map(int, input().split()))
    M = np.array([list(input()) for _ in range(H)])

    ans = 0
    for n in range(2**(H+W)):
        p = bin(n)[2:]
        p = '0'*(H+W-len(p)) + p
        m = M.copy()
        for i in range(H):
            for j in range(W):
                if p[i] == '1' or p[H+j] == '1':
                    m[i][j] = '.'
        cnt = np.count_nonzero(m == '#')
        if cnt == K:
            ans += 1

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
