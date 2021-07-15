import bisect
from itertools import accumulate


N, M = list(map(int, input().split()))
A = sorted(map(int, input().split()))

S = [0] + list(accumulate(A))


def calc(x):
    _total = 0
    _num = 0
    for i in range(N):
        j = bisect.bisect_left(A, x - A[i])
        _num += N - j
        _total += S[N] - S[j]
        _total += A[i] * (N - j)
    return _total, _num


left = 0
right = 200005

while right - left > 1:
    center = (left + right) // 2
    if calc(center)[1] >= M:
        left = center
    else:
        right = center

total, num = calc(left)
ans = total
ans -= (num - M) * left
print(ans)

