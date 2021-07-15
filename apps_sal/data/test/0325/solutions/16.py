import sys
import numpy as np
from scipy.sparse.csgraph import bellman_ford, connected_components
input = sys.stdin.readline


def main():
    n, m, p = list(map(int, input().split()))
    
    l = np.zeros((n, n))
    for i in range(m):
        a, b, c =list(map(int, input().split()))
        c = p-c
        if c == 0:
            c = 10**(-7.9)
        if l[a-1][b-1] == 0:
            l[a-1][b-1] = c
        else:
            l[a-1][b-1] = min(l[a-1][b-1], c)
    x = l[-1, 0]
    l[-1][0] = 10**(-7.9)
    n, labels = connected_components(l, connection="strong")
    l = l[labels == labels[0]][:, labels == labels[0]]
    l[-1, 0] = x
    
    try:
        print((max(0, int(round(bellman_ford(l, indices=0)[-1]))*(-1))))
    except:
        print((-1))


def __starting_point():
    main()

__starting_point()
