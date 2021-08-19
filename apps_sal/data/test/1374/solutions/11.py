import numpy as np
from collections import defaultdict
N = int(input())
A = np.array(input().split(), dtype=np.int32)
total_medians = N * (N + 1) // 2


def test(x):
    current = 0
    memo = defaultdict(int)
    memo[0] = 1
    cnt_below = 1
    result = 0
    for a in A:
        if a > x:
            current += 1
            cnt_below += memo[current]
        else:
            cnt_below -= memo[current]
            current -= 1
        result += cnt_below
        memo[current] += 1
        cnt_below += 1
    return result <= (total_medians - 1) // 2


AA = sorted(A)
left = -1
right = len(AA) - 1
while right - left > 1:
    mid = (left + right) // 2
    if test(AA[mid]):
        right = mid
    else:
        left = mid
answer = AA[right]
print(answer)
