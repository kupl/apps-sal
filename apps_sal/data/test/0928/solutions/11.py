import bisect as bi
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
R = [A[0]] * n
for i in range(n - 1):
    R[i + 1] = R[i] + A[i + 1]


def get(x):
    if x == 0:
        return 0
    return R[x - 1]


left = 0
right = 1
ans = 0
while 1:
    # if get?
    q = bi.bisect_left(R, get(left) + k)
    if q == n:
        print(ans)
        return
    ans += n - q
    left += 1
