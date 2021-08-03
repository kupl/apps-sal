from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))


def chk(L):
    cnt = 0
    for i in range(N):
        cnt += ceil(A[i] / L) - 1
    return cnt <= K


l, r = 1, max(A)
while l <= r:
    m = (l + r) // 2
    if chk(m):
        r = m - 1
    else:
        l = m + 1
print(min([x for x in [m - 1, m, m + 1] if x > 0 and chk(x)]))
