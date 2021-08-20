t = int(input())


def check(n, h, g, b, m):
    if m < n:
        return False
    (loop, rest) = divmod(m, g + b)
    ok = min(rest, g) + loop * g
    return ok >= h


for _ in range(t):
    (n, g, b) = list(map(int, input().split()))
    high = (n + 1) // 2
    (ok, ng) = (10 ** 20, 0)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(n, high, g, b, mid):
            ok = mid
        else:
            ng = mid
    print(ok)
