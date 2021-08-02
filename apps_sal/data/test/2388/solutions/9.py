n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)] + [(1 << 31, 0)]
mod = 998244353
l.sort()
st = [n]
dp = [0] * n + [1]
for i in range(n - 1, -1, -1):
    x, d = l[i]
    v = x + d
    while l[st[-1]][0] < v: st.pop()
    dp[i] = (dp[i + 1] + dp[st[-1]]) % mod
    st.append(i)
print(dp[0])
