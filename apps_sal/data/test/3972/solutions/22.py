MOD = 10 ** 9 + 7
n = int(input())
'\ndp = [-1] * (n + 1)\ndp[0] = 1\ndef cnt(num):\n    ans = 0\n    if num < 0:\n        return 1\n    if dp[num] != -1:\n        return dp[num]\n    if num == 1:\n        dp[num] = n\n        return n\n      \n    for i in range(n):\n        if i == 0:\n            ans += cnt(num - 1)\n            ans %= MOD\n        else:\n            if num - 2 - i < 0:\n                ans += 1\n            else:\n                ans += cnt(num - 2 - i)\n            ans += n - 1\n            ans %= MOD\n    dp[num] = ans\n    return ans\n\ndp[0] = 1\nprint(cnt(n))\n'
dq = [0] * (n + 1)
sum_ = [0] * (n + 1)
dq[0] = 1
sum_[0] = 1
for i in range(n):
    if i == 0:
        dq[i + 1] = n
        sum_[i + 1] = sum_[i] + dq[i + 1]
        continue
    '\n    for j in range(n):\n        if j == 0:\n            dq[i + 1] += dq[i]\n        else:\n            if i - 1 - j < 0:\n                dq[i + 1] += 1\n            else:\n                dq[i + 1] += dq[i - 1 - j]\n            dq[i + 1] += n - 1\n    '
    dq[i + 1] += dq[i]
    dq[i + 1] += (n - 1) * (n - 1)
    dq[i + 1] += sum_[i - 2]
    dq[i + 1] += abs(i - n)
    dq[i + 1] %= MOD
    sum_[i + 1] = sum_[i] + dq[i + 1]
    sum_[i + 1] %= MOD
print(dq[-1])
