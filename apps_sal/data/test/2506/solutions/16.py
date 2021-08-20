import bisect
(N, M) = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
A.sort(reverse=True)
As = [0] * (N + 1)
for i in range(N):
    As[i + 1] = As[i] + A[i]
A.reverse()


def flag(x):
    ans = 0
    for i in range(N):
        a = x - A[i]
        res = bisect.bisect_left(A, a)
        ans += N - res
    return bool(ans >= M)


def an(x):
    ans = 0
    m = 0
    for i in range(N):
        a = x - A[i]
        res = bisect.bisect_left(A, a)
        m += N - res
        ans += As[N - res]
        ans += A[i] * (N - res)
    ans -= (m - M) * x
    return ans


low = 0
high = 10 ** 6
while low <= high:
    mid = (low + high) // 2
    if flag(mid):
        if not flag(mid + 1):
            ans = mid
            break
        else:
            low = mid + 1
    else:
        high = mid - 1
print(an(ans))
