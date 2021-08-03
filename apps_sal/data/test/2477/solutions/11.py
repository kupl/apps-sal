from math import ceil


def check(x):
    cnt = 0
    for a in A:
        cnt += ceil(a / x) - 1
    return cnt <= K


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

left = 0
right = max(A)
while left < right - 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)
