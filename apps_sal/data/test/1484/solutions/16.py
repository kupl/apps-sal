import sys
input = sys.stdin.readline


def compress(string):
    n = len(string)
    (begin, cnt) = (0, 0)
    ans = []
    if n == 0:
        return ans
    for end in range(n + 1):
        if end == n or string[begin] != string[end]:
            ans.append((string[begin], cnt))
            (begin, cnt) = (end, 1)
        else:
            cnt += 1
    return ans


(n, k) = map(int, input().split())
a = list(map(int, input().split()))
MOD = 998244353
dp = [[0] * 2 for i in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    dp[i + 1][0] += dp[i][1]
    dp[i + 1][0] %= MOD
    dp[i + 1][1] += dp[i][0] * (k - 1)
    dp[i + 1][1] += dp[i][1] * (k - 2)
    dp[i + 1][1] %= MOD
dq = [0 for i in range(n + 1)]
dq[1] = k
for i in range(1, n):
    dq[i + 1] += dq[i] * (k - 1)
    dq[i + 1] %= MOD
odd = []
even = []
for (i, val) in enumerate(a):
    if i % 2 == 0:
        odd.append(val)
    else:
        even.append(val)
ans = 1
odd = compress(odd)
for (i, (val, cnt)) in enumerate(odd):
    if val != -1 and cnt > 1:
        ans = 0
        continue
    if val != -1:
        continue
    else:
        if i == 0:
            tmp = dq[cnt]
            if i + 1 == len(odd):
                ans *= tmp
                ans %= MOD
            else:
                ans *= tmp * pow(k, MOD - 2, MOD) * (k - 1)
                ans %= MOD
            continue
        (tmp1, tmp2) = dp[cnt]
        if cnt == 1:
            if i + 1 == len(odd):
                ans *= tmp2
                ans %= MOD
            elif odd[i + 1][0] == odd[i - 1][0]:
                ans *= tmp2
                ans %= MOD
            elif odd[i + 1][0] != odd[i - 1][0]:
                ans *= tmp2 * pow(k - 1, MOD - 2, MOD) * (k - 2)
                ans %= MOD
        elif i + 1 == len(odd):
            ans *= tmp1 + tmp2
            ans %= MOD
        elif odd[i + 1][0] == odd[i - 1][0]:
            ans *= tmp2
            ans %= MOD
        elif odd[i + 1][0] != odd[i - 1][0]:
            ans *= tmp1 + tmp2 * pow(k - 1, MOD - 2, MOD) * (k - 2)
            ans %= MOD
odd = compress(even)
for (i, (val, cnt)) in enumerate(odd):
    if val != -1 and cnt > 1:
        ans = 0
        continue
    if val != -1:
        continue
    else:
        if i == 0:
            tmp = dq[cnt]
            if i + 1 == len(odd):
                ans *= tmp
                ans %= MOD
            else:
                ans *= tmp * pow(k, MOD - 2, MOD) * (k - 1)
                ans %= MOD
            continue
        (tmp1, tmp2) = dp[cnt]
        if cnt == 1:
            if i + 1 == len(odd):
                ans *= tmp2
                ans %= MOD
            elif odd[i + 1][0] == odd[i - 1][0]:
                ans *= tmp2
                ans %= MOD
            elif odd[i + 1][0] != odd[i - 1][0]:
                ans *= tmp2 * pow(k - 1, MOD - 2, MOD) * (k - 2)
                ans %= MOD
        elif i + 1 == len(odd):
            ans *= tmp1 + tmp2
            ans %= MOD
        elif odd[i + 1][0] == odd[i - 1][0]:
            ans *= tmp2
            ans %= MOD
        elif odd[i + 1][0] != odd[i - 1][0]:
            ans *= tmp1 + tmp2 * pow(k - 1, MOD - 2, MOD) * (k - 2)
            ans %= MOD
print(ans % MOD)
