(n, k) = map(int, input().split())
s = input()


def f(x, y):
    if x == y:
        return x
    elif (x, y) == ('R', 'S') or (x, y) == ('S', 'P') or (x, y) == ('P', 'R'):
        return x
    else:
        return y


dp = [[''] * n for _ in range(k + 1)]
for i in range(n):
    dp[0][i] = s[i]


def g(x, k):
    if dp[k][x] != '':
        return dp[k][x]
    a = x % n
    b = (x + pow(2, k - 1, n)) % n
    p = g(a, k - 1)
    q = g(b, k - 1)
    dp[k][x] = f(p, q)
    return dp[k][x]


g(0, k)
print(dp[k][0])
