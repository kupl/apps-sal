import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    res = 1
    if n == k:
        for a in A:
            res = (res * a) % mod
        print(res)
        return

    P, M = [], []
    for a in A:
        P.append(a) if a >= 0 else M.append(a)

    if len(P) == n:
        A.sort(reverse=True)
        for i in range(k):
            res = (res * A[i]) % mod
    elif len(M) == n:
        A.sort(reverse=True) if k % 2 else A.sort()
        for i in range(k):
            res = (res * A[i]) % mod
    else:
        P.sort(reverse=True)
        M.sort()
        B = []
        if k % 2:
            k -= 1
            b = P.pop(0)
            B.append(b)
            res = (res * b) % mod
        for i in range(0, len(P), 2):
            if i + 1 < len(P):
                B.append(P[i] * P[i + 1])
        for j in range(0, len(M), 2):
            if j + 1 < len(M):
                B.append(M[j] * M[j + 1])
        B.sort(reverse=True)
        for i in range(k // 2):
            res = (res * B[i]) % mod

    print(res)

def __starting_point():
    resolve()

__starting_point()
