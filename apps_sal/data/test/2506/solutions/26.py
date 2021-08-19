from itertools import accumulate
from bisect import bisect_left, bisect_right
(N, M) = list(map(int, input().split()))
(*A,) = list(map(int, input().split()))
A.sort()
acc = list(accumulate(A[::-1]))[::-1] + [0]


def isok(x):
    cnt = 0
    for a in A:
        cnt += N - bisect_left(A, x - a)
    return cnt >= M


l = 0
r = 202020
while l + 1 < r:
    m = (l + r) // 2
    if isok(m):
        l = m
    else:
        r = m
ans = 0
cnt = 0
for a in A:
    i = bisect_left(A, l - a)
    ans += a * (N - i) + acc[i]
    cnt += N - i
if cnt > M:
    ans -= l * (cnt - M)
print(ans)
