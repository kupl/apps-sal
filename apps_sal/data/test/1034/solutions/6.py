import numpy as np


def main():
    (X, Y, Z, K) = list(map(int, input().split(' ')))
    A = np.array(list(map(int, input().split(' '))))
    B = np.array(list(map(int, input().split(' '))))
    C = np.array(list(map(int, input().split(' '))))
    AB = np.array(np.meshgrid(A, B)).T.reshape(-1, 2).sum(axis=1)
    AB[::-1].sort()
    AB = AB[:min([K, X * Y])]
    ABC = np.array(np.meshgrid(AB, C)).T.reshape(-1, 2).sum(axis=1)
    ABC[::-1].sort()
    for ans in ABC[:K]:
        print(ans)


def __starting_point():
    main()


__starting_point()
