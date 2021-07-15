import numpy as np
def main():
    n = int(input())
    P = np.fromstring(input(), np.int64, sep=' ')
    D = np.arange(1, n+1) - P
    if np.any(D == 0) or D[D > 0].sum() != n-1:
        print((-1))
        return
    if np.any(np.diff(P[D<0]) < 0) or np.any(np.diff(P[D>0]) < 0):
        print((-1))
        return
    for i in np.nonzero(D>0)[0]:
        j = i
        for _ in range(D[i]):
            print(j)
            j -= 1

def __starting_point():
    main()

__starting_point()
