(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))


def isOK(x):
    cnt = 0
    for a in A:
        cnt += (a + x - 1) // x - 1
    return cnt <= K


(left, right) = (0, 10 ** 10)
while right - left > 1:
    mid = (left + right) // 2
    if isOK(mid):
        right = mid
    else:
        left = mid
print(right)
