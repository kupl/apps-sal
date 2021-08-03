n, m = map(int, input().split())
a = set()
for _ in range(m):
    a.add(int(input()))

DP = [None] * 100001
DP[0] = 1
if 1 in a:
    DP[1] = 0
else:
    DP[1] = 1


def stairs(n):
    for i in range(2, n + 1):
        DP[i] = DP[i - 1] + DP[i - 2]
        if i in a:
            DP[i] = 0
        DP[i] %= 10**9 + 7
    return DP[n]


print(stairs(n))
