(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a = sorted(a)
f = sorted(f, reverse=True)


def is_lessthanK(X):
    ans = 0
    for (A, F) in zip(a, f):
        if A * F > X:
            ans += A - X // F
        if ans > k:
            return False
    return True


ng = -1
ok = a[-1] * f[0]
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_lessthanK(mid):
        ok = mid
    else:
        ng = mid
print(ok)
