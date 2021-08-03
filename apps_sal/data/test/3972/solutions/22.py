MOD = 10 ** 9 + 7
n = int(input())

"""
dp = [-1] * (n + 1)
dp[0] = 1
def cnt(num):
    ans = 0
    if num < 0:
        return 1
    if dp[num] != -1:
        return dp[num]
    if num == 1:
        dp[num] = n
        return n
      
    for i in range(n):
        if i == 0:
            ans += cnt(num - 1)
            ans %= MOD
        else:
            if num - 2 - i < 0:
                ans += 1
            else:
                ans += cnt(num - 2 - i)
            ans += n - 1
            ans %= MOD
    dp[num] = ans
    return ans

dp[0] = 1
print(cnt(n))
"""

dq = [0] * (n + 1)
sum_ = [0] * (n + 1)
dq[0] = 1
sum_[0] = 1
for i in range(n):
    if i == 0:
        dq[i + 1] = n
        sum_[i + 1] = sum_[i] + dq[i + 1]
        continue
    """
    for j in range(n):
        if j == 0:
            dq[i + 1] += dq[i]
        else:
            if i - 1 - j < 0:
                dq[i + 1] += 1
            else:
                dq[i + 1] += dq[i - 1 - j]
            dq[i + 1] += n - 1
    """
    dq[i + 1] += dq[i]
    dq[i + 1] += (n - 1) * (n - 1)
    dq[i + 1] += sum_[i - 2]
    dq[i + 1] += abs(i - n)
    dq[i + 1] %= MOD
    sum_[i + 1] = sum_[i] + dq[i + 1]
    sum_[i + 1] %= MOD

print((dq[-1]))
