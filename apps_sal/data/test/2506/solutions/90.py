from bisect import bisect_left as BL
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()


def isok(border):
    res = 0
    for i in range(N):
        res += N - BL(A, border - A[i])
    return res >= M


ok = 0
ng = A[-1] * 2 + 1
mid = (ok + ng) // 2
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid
B = reversed(A)
SB = [0]
for b in B:
    SB.append(b + SB[-1])
ans = 0
shake_c = 0
for i in range(N):
    goodshake = N - BL(A, ok - A[i])
    shake_c += goodshake
    ans += A[i] * goodshake
    ans += SB[goodshake]
ans -= (shake_c - M) * ok
print(ans)
