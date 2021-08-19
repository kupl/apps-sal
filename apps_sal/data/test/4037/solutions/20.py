(N, R) = [int(x) for x in input().split()]
projects = [[int(x) for x in input().split()] for _ in range(N)]
pos = []
neg = []
for (a, b) in projects:
    if b < 0:
        neg.append((a, b))
    else:
        pos.append((a, b))
pos.sort()
ans = 0
for (a, b) in pos:
    if R >= a:
        R += b
        ans += 1
neg.sort(key=sum, reverse=True)
memo = {}


def dp(i, r):
    if (i, r) in memo:
        return memo[i, r]
    if i == len(neg):
        return 0
    (a, b) = neg[i]
    ans = dp(i + 1, r)
    if r >= a and r + b >= 0:
        ans = max(ans, dp(i + 1, r + b) + 1)
    memo[i, r] = ans
    return ans


print(dp(0, R) + ans)
