import sys
K = int(input())
X, Y = map(int, input().split())
if (X + Y) % 2 and K % 2 == 0:
    print(-1)
    return


def solve(K, X, Y):
    if (X + Y) % 2 and K % 2 == 0:
        return None

    def gen(a, b, c, d):
        ans = []
        x = y = 0
        assert c - a == Y and b - d == X
        while a >= K:
            y -= K
            a -= K
            ans.append((0, y))
        if a:
            x += K - a
            y -= a
            b -= K - a
            ans.append((x, y))
        while b >= K:
            x += K
            b -= K
            ans.append((x, y))
        if b:
            x += b
            y += K - b
            c -= K - b
            ans.append((x, y))
        while c >= K:
            y += K
            c -= K
            ans.append((x, y))
        if c:
            x -= K - c
            y += c
            d -= K - c
            ans.append((x, y))
        while d >= K:
            x -= K
            d -= K
            ans.append((x, y))
        assert X == x and Y == y, (x, y, ans)
        assert d == 0
        return ans

    ans = []
    if X + Y < K:
        if (X + Y) % 2 == 1:
            n = 3
            ans = gen(K - X, X + (K + X - Y) // 2, K - X + Y, (K + X - Y) // 2)
        else:
            n = 2
            ans = gen((K * n - X - Y) // 2, X, (K * n - X + Y) // 2, 0)
    else:
        c = (K - (X + Y)) % K
        if c % 2 == 1:
            n = (X + Y + K - 1) // K + 1
        else:
            n = (X + Y + K - 1) // K
        ans = gen((K * n - X - Y) // 2, X, (K * n - X + Y) // 2, 0)
    assert len(ans) == n
    return ans


rx = X < 0
if rx:
    X = -X
ry = Y < 0
if ry:
    Y = -Y
r = X < Y
if r:
    X, Y = Y, X
ans = solve(K, X, Y)
if ans:
    print(len(ans))
    for x, y in ans:
        if r:
            x, y = y, x
        if rx:
            x = -x
        if ry:
            y = -y
        print(x, y)
else:
    print(-1)
