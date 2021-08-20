import sys
input = sys.stdin.readline
Q = int(input())
Query = []
for _ in range(Q):
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))
for (N, K, A) in Query:
    Inds = []
    exists = False
    for (i, a) in enumerate(A):
        if a == K:
            exists = True
        if a >= K:
            Inds.append(i)
    if not exists:
        ok = False
    elif N == 1:
        ok = True
    else:
        ok = False
        for ind in Inds:
            if ind < N - 1 and A[ind + 1] >= A[ind]:
                ok = True
            elif ind > 0 and A[ind - 1] >= A[ind]:
                ok = True
            elif ind > 1 and A[ind - 2] >= A[ind]:
                ok = True
            elif ind < N - 2 and A[ind + 2] >= A[ind]:
                ok = True
    print('yes' if ok else 'no')
