import bisect
from itertools import accumulate
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
A2 = [0] + list(accumulate(A))


def judge(mid):
    count = 0
    for i in range(N):
        border = mid - A[i]
        ind = bisect.bisect_left(A, border)
        count += N - ind
    if count < M:
        return True
    else:
        return False


mina = 0
maxa = 2 * (10**5) + 1
while maxa - mina > 1:
    mid = (maxa + mina) // 2
    if judge(mid):
        maxa = mid
    else:
        mina = mid
count = 0
ans = 0
for i in range(N):
    border = maxa - A[i]
    ind = bisect.bisect_left(A, border)
    count += N - ind
    ans += A[i] * (N - ind) + A2[N] - A2[ind]
if count == M:
    print(ans)
else:
    rem = M - count
    print(ans + rem * mina)
