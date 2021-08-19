def cin():
    return list(map(int, input().split()))


n = int(input())
st = input()
a = list(cin())
dp = [0] * (n + 2)
mn = [10 ** 4] * (n + 2)
mx = 1
dp[0] = 1
dp[-1] = 1
mn[0] = 1
mn[-1] = 0
mod = int(1000000000.0) + 7
for i in range(1, n):
    c = 10 ** 4
    for j in range(i, -1, -1):
        ind = ord(st[j]) - ord('a')
        c = min(c, a[ind])
        if c < i - j + 1:
            break
        dp[i] += dp[j - 1]
        mn[i] = min(mn[i], mn[j - 1] + 1)
        mx = max(mx, i - j + 1)
print('\n'.join(map(str, [dp[n - 1] % mod, mx, mn[n - 1]])))
