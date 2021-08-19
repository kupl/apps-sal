import bisect
import sys
readline = sys.stdin.readline
(N, M) = map(int, readline().split())
A = sorted(list(map(int, readline().split())))
ok = -1
ng = 10 ** 5 * 2 + 1


def isOk(x):
    cnt = 0
    for left in A:
        right = x - left
        ind = bisect.bisect_left(A, right)
        cnt += N - ind
    return cnt >= M


while abs(ng - ok) > 1:
    mid = abs(ng + ok) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid
sumA = [0] + A.copy()
for i in range(1, len(sumA)):
    sumA[i] += sumA[i - 1]
ans = 0
num = 0
for left in A:
    right = ok - left
    ind = bisect.bisect_left(A, right)
    num += N - ind
    ans += (N - ind) * left + sumA[-1] - sumA[ind]
if num > M:
    ans -= (num - M) * ok
print(ans)
