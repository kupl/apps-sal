import sys
sys.setrecursionlimit(300000)


def solve(x, y, k):
    if x == y == 0:
        return []
    if x < 0:
        return [(-x, y) for (x, y) in solve(-x, y, k)]
    if y < 0:
        return [(x, -y) for (x, y) in solve(x, -y, k)]
    if x > y:
        return [(x, y) for (y, x) in solve(y, x, k)]
    if (x + y) % k == 0:
        return [(k, 0)] * (x // k) + [(0, k)] * (y // k) + ([] if x % k == y % k == 0 else [(x % k, y % k)])
    if x + y >= 2 * k:
        if x % k + y % k >= k:
            return [(k, 0)] * (x // k) + [(0, k)] * (y // k) + solve(x % k, y % k, k)
        else:
            return ([(k, 0)] * (x // k) + [(0, k)] * (y // k))[:-1] + solve(x % k, y % k + k, k)
    if x + y < K and (x + y) % 2 == 1:
        return solve(x, y + k, k) + [(0, -k)]
    if K & 1 and x + y > k and ((x + y) % k % 2 == 0):
        return solve(x, y - k, k) + [(0, k)]
    z = (x + y) // 2
    return [(k - z + x, z - x), (z - k, z)]


(K, X, Y) = map(int, open(0).read().split())
if K % 2 == 0 and (X + Y) % 2 == 1:
    print(-1)
else:
    ans = solve(X, Y, K)
    print(len(ans))
    (ax, ay) = (0, 0)
    for (x, y) in ans:
        ax += x
        ay += y
        print(ax, ay)
