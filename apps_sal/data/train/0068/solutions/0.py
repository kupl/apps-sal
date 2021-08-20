from itertools import groupby


def main():
    N = int(input())
    S = input()
    C = [len(list(x[1])) for x in groupby(S)]
    M = len(C)
    dup_idx = []
    for (i, c) in enumerate(C):
        if c > 1:
            dup_idx.append(i)
    dup_idx.reverse()
    curr = 0
    while dup_idx:
        i = dup_idx[-1]
        if i < curr:
            dup_idx.pop()
            continue
        C[i] -= 1
        if C[i] == 1:
            dup_idx.pop()
        curr += 1
    ans = curr + (M - curr + 1) // 2
    print(ans)


def __starting_point():
    for __ in [0] * int(input()):
        main()


__starting_point()
