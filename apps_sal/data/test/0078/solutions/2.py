from functools import lru_cache
P = 10 ** 9 + 7
(N, T) = map(int, input().split())
A = [[], [], []]
X = []
for _ in range(N):
    (t, g) = map(int, input().split())
    X.append((t, g))


@lru_cache(maxsize=None)
def calc(x, pr, t):
    if t < 0:
        return 0
    if t == 0:
        return 1
    if x == 0:
        return 0
    ans = 0
    for i in range(15):
        if x & 1 << i:
            if X[i][1] != pr:
                y = x ^ 1 << i
                ans = (ans + calc(y, X[i][1], t - X[i][0])) % P
    return ans


print(calc(2 ** N - 1, -1, T))
