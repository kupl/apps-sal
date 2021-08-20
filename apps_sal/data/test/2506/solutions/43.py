from itertools import accumulate
import bisect
import sys
input = sys.stdin.readline
(N, M) = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()
left = -1
right = 1 + 2 * 10 ** 5


def shake(x):
    cnt = 0
    for i in A:
        cnt += N - bisect.bisect_left(A, x - i)
    if cnt >= M:
        return 1
    else:
        return 0


while True:
    mid = (left + right) // 2
    if shake(mid):
        if not shake(mid + 1):
            X = mid
            break
        else:
            left = mid
    elif shake(mid - 1):
        X = mid - 1
        break
    else:
        right = mid
happy = 0
cumsum_A = list(accumulate(A))
for j in A:
    idx = bisect.bisect_right(A, X - j)
    cnt = N - idx
    if cnt == N:
        happy += cumsum_A[-1] + cnt * j
    else:
        happy += cumsum_A[-1] - cumsum_A[idx - 1] + cnt * j
    M -= cnt
happy += M * X
print(happy)
