def solve(a, b, mid):

    a -= mid
    b -= mid
    if a < 0 or b < 0:
        return False
    if a + b >= mid:
        return True
    else:
        return False


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ok = 0
    ng = 10 ** 10
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(a, b, mid):
            ok = mid
        else:
            ng = mid
    print(ok)
