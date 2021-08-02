import numpy as np


def main():
    n, m, q = map(int, input().split())
    lst = np.zeros((n, n), dtype=int)

    for _ in range(m):
        s, t = map(int, input().split())
        lst[s - 1][t - 1] += 1
    lst = lst.cumsum(axis=1)[::-1].cumsum(axis=0)[::-1]

    for _ in range(q):
        s, t = map(int, input().split())
        print(lst[s - 1][t - 1])


main()
