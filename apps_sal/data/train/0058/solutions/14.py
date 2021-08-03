dp = {}


def getDP(n, m, k):
    if (n, m, k) in dp:
        return dp[(n, m, k)]
    elif (m, n, k) in dp:
        return dp[(m, n, k)]
    return None


def solve(n, m, k):
    if n == 2 and m == 3 and k == 5:
        h = 5
    if k == m * n or k == 0:
        dp[(n, m, k)] = 0
    elif k % min(n, m) == 0:
        dp[(n, m, k)] = min(n, m) ** 2
    elif k == 1:
        dp[(n, m, k)] = min(n, m) ** 2 + 1
    elif getDP(n, m, k) is not None:
        return getDP(n, m, k)
    else:
        bestAns = float('inf')
        for i in range(1, n):
            if k <= i * m:
                bestAns = min(bestAns, getDP(i, m, k) + m ** 2)
            else:
                bestAns = min(bestAns, getDP(n - i, m, k - i * m) + m ** 2)

        for i in range(1, m):
            if k <= i * n:
                bestAns = min(bestAns, getDP(i, n, k) + n ** 2)
            else:
                bestAns = min(bestAns, getDP(m - i, n, k - i * n) + n ** 2)
        dp[(n, m, k)] = bestAns


for i in range(1, 31):
    for j in range(1, 31):
        for k in range(min(i * j, 50) + 1):
            solve(i, j, k)
toPrint = []
t = int(input())
for i in range(t):
    n, m, k = [int(x) for x in input().split(" ")]
    toPrint.append(getDP(n, m, k))

for x in toPrint:
    print(x)
