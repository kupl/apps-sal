import sys


def main(N, P):
    I = [-1] * N
    for i, p in enumerate(P): I[p] = i
    p = 0
    s = 0
    ans = []
    while s < N:
        i = I[p]
        if s == i:
            p += 1
            s += 1
            continue
        for j in range(i, s, -1):
            ans.append(j)
        p += 1
        for j in range(s, i - 1):
            if P[j] != p:
                return None
            p += 1
        s = i
        p = s
        P[i] = P[i - 1]
        I[P[i]] = i
    if len(ans) != N - 1:
        return None
    return ans


def __starting_point():
    input = sys.stdin.readline
    N = int(input())
    *P, = [int(x) - 1 for x in input().split()]
    ans = main(N, P)
    if ans is None:
        print((-1))
    else:
        for a in ans:
            print(a)


__starting_point()
