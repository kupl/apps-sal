from bisect import bisect_left
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
l = 1
r = 200000 + 1


def chk(x):
    c = 0
    for la in A:
        y = bisect_left(A, x - la)
        c += N - y
    if c >= M:
        return True
    else:
        return False


while l + 1 < r:
    mid = (l + r) // 2
    if chk(mid):
        l = mid
    else:
        r = mid
AN = l
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]
ans1 = 0
c = 0
for la in A:
    ll = -1
    rr = N
    while ll + 1 < rr:
        mi = (ll + rr) // 2
        if A[mi] > AN - la:
            rr = mi
        else:
            ll = mi
    c += N - rr
    ans1 = ans1 + la * (N - rr) + S[N] - S[rr]
ans = ans1 + (M - c) * AN
print(ans)
