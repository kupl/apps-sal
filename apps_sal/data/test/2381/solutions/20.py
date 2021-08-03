from collections import defaultdict


def prod(A, k, mod):
    ans = 1
    for i in range(k):
        ans *= A[i]
        ans %= mod
    return ans


def solve():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 1
    if K == N:
        return prod(A, N, mod)
    minus = len([a for a in A if a < 0])
    if minus == N:
        if K % 2 == 0:
            A.sort()
        else:
            A.sort(reverse=True)
        return prod(A, K, mod)
    if K == 1:
        return max(A)
    A.sort(key=lambda x: -abs(x))
    if A[K] == 0:
        return 0
    minus = len([a for a in A[:K] if a < 0])
    flag = [1] * K + [0] * (N - K)
    d = defaultdict(lambda: -1)
    if minus % 2 == 1:
        for i in range(K, N):
            if A[i] >= 0:
                d['p2'] = i
                break
        for i in range(K, N):
            if A[i] < 0:
                d['m2'] = i
                break
        for i in range(K - 1, -1, -1):
            if A[i] > 0:
                d['p1'] = i
                break
        for i in range(K - 1, -1, -1):
            if A[i] < 0:
                d['m1'] = i
                break
        if d['p2'] == -1 or d['m1'] == -1:
            flag[d['m2']], flag[d['p1']] = 1, 0
        elif d['m2'] == -1 or d['p1'] == -1:
            flag[d['p2']], flag[d['m1']] = 1, 0
        elif A[d['p2']] * A[d['p1']] > A[d['m1']] * A[d['m2']]:
            flag[d['p2']], flag[d['m1']] = 1, 0
        else:
            flag[d['m2']], flag[d['p1']] = 1, 0
        ans = 1
        for i in range(N):
            if flag[i] == 1:
                ans *= A[i]
                ans %= mod
        return ans
    return prod(A, K, mod)


print((solve()))
