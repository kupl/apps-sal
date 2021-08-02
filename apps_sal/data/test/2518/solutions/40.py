import math

N, A, B = map(int, input().split())
h = [int(input()) for i in range(N)]


def C(T):
    t = 0
    for i in range(N):
        if h[i] > B * T:
            t += math.ceil((h[i] - B * T) / (A - B))
    if t <= T:
        return True
    else:
        False


l, r = 0, 10**18
while r - l > 1:
    mid = (l + r) // 2
    if C(mid):
        r = mid
    else:
        l = mid


print(r)
