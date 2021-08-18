

import itertools


def main():
    N, K = [int(n) for n in input().split(" ")]
    D = [1] * 10
    for d in input().split(" "):
        D[int(d)] = 0
    L = [str(i) for i, v in enumerate(D) if v == 1]

    digit = len(str(N))
    cand = []
    for n in list(itertools.product(L, repeat=digit)):
        p = int("".join(list(n)))
        if p >= N:
            cand.append(p)
    if len(cand):
        print((min(cand)))
    else:
        if L[0] == "0":
            print((str(L[1]) + "0" * digit))
        else:
            print((str(L[0]) * (digit + 1)))


main()
