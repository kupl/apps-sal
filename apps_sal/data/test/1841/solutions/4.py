__author__ = 'sm'


def readln():
    return list(map(int, input().split()))


n, m = readln()
data = readln()

dp = [0] * n

dp[n - 1] = 1
cache = set()
cache.add(data[n - 1])

i = n - 2
while i >= 0:
    if data[i] in cache:
        dp[i] = dp[i + 1]
    else:
        dp[i] = dp[i + 1] + 1
        cache.add(data[i])
    i -= 1

ans = []
for i in range(m):
    idx = readln()[0]
    ans.append(str(dp[idx - 1]))

print('\n'.join(ans))
