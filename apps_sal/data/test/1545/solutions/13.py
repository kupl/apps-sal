M = 10 ** 9 + 7


def o(i):
    return ord(s[i]) - 97


n = int(input())
s = input()
a = [int(item) for item in input().split()]
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
mn = float('inf')
longest = -float('inf')
maxNb = 1
ii = 1
tmp = a[o(0)]
if a[o(0)] == 1 and n != 1:
    maxNb += 1
    tmp = float('inf')
    ii = 0
if n == 1:
    longest = 1
for i in range(2, n + 1):
    ii += 1
    j = 0
    mn = a[o(i - 1)]
    k = -1
    while j <= i and j <= mn:
        mn = min(mn, a[o(i - j - 1)])
        dp[i] += dp[i - j] % M
        j += 1
        k += 1
    dp[i] %= M
    longest = max(longest, k)
    tmp = min(tmp, a[o(i - 1)])
    if i == n:
        break
    if tmp == ii:
        ii = 0
        tmp = float('inf')
        maxNb += 1
    elif tmp < ii:
        ii = 1
        maxNb += 1
        tmp = a[o(i - 1)]
        if i == n - 1:
            maxNb += 1
    elif i == n - 1:
        if a[o(i)] < ii + 1:
            maxNb += 1
print(dp[n] % M)
print(longest)
print(maxNb)
