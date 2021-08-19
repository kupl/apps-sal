from itertools import accumulate


def solve():
    (a, b, q) = map(int, input().split())
    tb = [int(i % a % b != i % b % a) for i in range(a * b)]
    bs = sum(tb)
    tb += tb
    tbs = [0] + list(accumulate(tb))
    res = []
    for i in range(q):
        (l, r) = map(int, input().split())
        r += 1
        w = (r - l) // (a * b)
        ans = w * bs
        r -= w * a * b
        u = l // (a * b)
        l %= a * b
        r -= u * (a * b)
        ans += tbs[r] - tbs[l]
        res.append(ans)
    print(*res)


t = int(input())
for _ in range(t):
    solve()
