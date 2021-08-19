import bisect
import sys
readline = sys.stdin.readline
(N, M) = list(map(int, readline().split()))
A = sorted(list(map(int, readline().split())))
sumA = [0] + A.copy()
for i in range(1, len(sumA)):
    sumA[i] += sumA[i - 1]
ok = -1
ng = 10 ** 5 * 2 + 1


def isOk(x):
    cnt = 0
    for left in A:
        right = x - left
        ind = bisect.bisect_left(A, right)
        cnt += N - ind
    if cnt > M:
        return True
    else:
        return False


while abs(ng - ok) > 1:
    mid = abs(ng + ok) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid
ans = 0
num = 0
for left in A:
    right = ok - left
    ind = bisect.bisect_left(A, right)
    ans += sumA[-1] - sumA[ind] + (N - ind) * left
    num += N - ind
if num > M:
    ans -= (num - M) * ok
print(ans)
