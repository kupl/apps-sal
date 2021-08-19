import sys
sys.setrecursionlimit(10 ** 6)
(N, M, Q) = list(map(int, input().split()))
abcd = [list(map(int, input().split())) for i in range(Q)]
A = []


def rec(itr, lst):
    if itr == N:
        res = 0
        for (a, b, c, d) in abcd:
            if A[b - 1] - A[a - 1] == c:
                res += d
        return res
    else:
        res = 0
        for i in range(lst, M):
            A.append(i)
            res = max(res, rec(itr + 1, i))
            A.pop()
        return res


print(rec(0, 0))
