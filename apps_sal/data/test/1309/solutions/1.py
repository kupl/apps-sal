from itertools import combinations
N = 2 * int(input())
W = list(map(int, input().split()))
W.sort()


def it():
    for (i, j) in combinations(list(range(N)), r=2):
        k = 0
        cnt = 0
        w = None
        for k in range(N):
            if not (k == i or k == j):
                if w is None:
                    w = W[k]
                else:
                    cnt += abs(w - W[k])
                    w = None
        yield cnt


print(min(it()))
