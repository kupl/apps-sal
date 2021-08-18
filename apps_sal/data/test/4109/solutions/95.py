from itertools import combinations


def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        c, *A_ = list(map(int, input().split()))
        C.append(c)
        A.append(A_)

    ret = 10**9
    for m in range(1, N + 1):
        for comb in combinations(range(N), m):
            vec = [0] * M
            cost = 0
            for i in comb:
                for j, A_e in enumerate(A[i]):
                    vec[j] += A_e
                cost += C[i]

            if min(vec) >= X:
                ret = min(ret, cost)

    print(ret if ret < 10**9 else -1)


solve()
