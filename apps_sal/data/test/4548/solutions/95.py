import bisect
N, M, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

idx = bisect.bisect(A, X)

ans_r = len(A[idx:])
ans_l = len(A[:idx])

ans = min(ans_l, ans_r)
print(ans)
