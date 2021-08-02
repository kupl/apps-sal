import numpy as np
from numpy.fft import rfft, irfft


def main():
    n, m = map(int, input().split())
    A = np.array(list(map(int, input().split())))
    F = np.bincount(A)
    fft_len = 2 * 10**5 + 1
    Ff = rfft(F, fft_len)
    G = np.rint(irfft(Ff * Ff, fft_len)).astype(np.int64)
    G_acc = G.cumsum()
    remove_cnt = n**2 - m
    border = np.searchsorted(G_acc, n**2 - m)
    x = n**2 - m - G_acc[border - 1]
    remove_sum = (G[:border] * np.arange(border)).sum() + border * x
    ans = A.sum() * 2 * n - remove_sum
    print(ans)


def __starting_point():
    main()


__starting_point()
