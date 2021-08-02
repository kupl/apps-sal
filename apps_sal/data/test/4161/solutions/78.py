n = int(input())
memo = [[0] * (n + 1) for x in range(n + 1)]


def gcd(x, y):
    if y == 0:
        return x
    if not memo[x][y] == 0:
        return memo[x][y]
    memo[x][y] = gcd(y, x % y)
    return gcd(y, x % y)


res = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        q = gcd(i, j)
        if q == 1:
            res += n
        else:
            for k in range(1, n + 1):
                p = gcd(q, k)
                res += p
print(res)
