T = int(input())
for _ in range(T):
    A, B = list(map(int, input().split()))

    def is_ok(k):
        a = A - k
        b = B - k
        if a < 0 or b < 0:
            return False
        return a + b >= k
    ok = 0
    ng = 10**9
    while ng - ok > 1:
        m = (ok + ng) // 2
        if is_ok(m):
            ok = m
        else:
            ng = m
    print(ok)
