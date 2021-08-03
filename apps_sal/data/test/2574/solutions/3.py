from functools import reduce


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ng, ps = [], []
    for i in a:
        if i < 0:
            ng.append(-i)
        else:
            ps.append(i)
    ps.sort(reverse=True)
    ng.sort(reverse=True)
    ans = max(
        reduce(int.__mul__, ps[:5]) if len(ps) >= 5 else -10 ** 30,
        reduce(int.__mul__, ps[:3] + ng[:2]) if len(ps) >= 3 and len(ng) >= 2 else -10 ** 30,
        reduce(int.__mul__, ps[:1] + ng[:4]) if len(ps) >= 1 and len(ng) >= 4 else -10 ** 30
    )
    if 0 in a:
        ans = max(ans, 0)
    ps.sort()
    ng.sort()
    ans = max(
        ans,
        -reduce(int.__mul__, ps[:4] + ng[:1]) if len(ps) >= 4 and len(ng) >= 1 else -10 ** 30,
        -reduce(int.__mul__, ps[:2] + ng[:3]) if len(ps) >= 2 and len(ng) >= 3 else -10 ** 30,
        -reduce(int.__mul__, ng[:5]) if len(ng) >= 5 else -10 ** 30
    )
    print(ans)


t = int(input())
for _ in range(t):
    solve()
