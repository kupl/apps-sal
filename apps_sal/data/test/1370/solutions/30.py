import sys
import numpy as np
from itertools import combinations_with_replacement, product


def input():
    return sys.stdin.readline().rstrip()


def culc(array, k, count):
    array = array.T
    cuts = np.zeros(array.shape[1])
    for i in range(array.shape[0]):
        if any(array[i] > k):
            return 10 ** 6
        elif any(array[i] + cuts > k):
            cuts = array[i]
            count += 1
        else:
            cuts += array[i]
    return count


def main():
    (h, w, k) = map(int, input().split())
    choco = np.zeros((h, w))
    for i in range(h):
        choco[i] = list(input())
    ans = 10 ** 6
    choco = choco.astype(np.int64)
    for bit in product([0, 1], repeat=h - 1):
        if sum(bit) >= ans:
            break
        chocos = choco.copy()
        cut = chocos[0].reshape([1, w])
        for i in range(h - 1):
            if bit[i] == 1:
                cut = np.concatenate([cut, chocos[i + 1].reshape([1, w])])
            else:
                cut[-1] += chocos[i + 1]
        ans = min(ans, culc(cut, k, sum(bit)))
    print(ans)


def __starting_point():
    main()


__starting_point()
