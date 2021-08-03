n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

mod = 998244353
ans = 0
arr.sort(key=lambda x: x[0], reverse=True)
pos = [i[0] for i in arr]
moved = [sum(i) for i in arr]
children = [i for i in range(-1, n)]

for i in range(1, n):
    parent = moved[i]
    child = children[i]
    cmp = pos[child]
    while cmp < parent:
        child = children[child]
        if child == -1:
            break
        cmp = pos[child]
    children[i] = child

dp = [0] * (n + 1)
dp[n] = 1
for i in range(n):
    dp[i] = dp[i - 1] + dp[children[i]]
    dp[i] %= mod

print(dp[n - 1])
