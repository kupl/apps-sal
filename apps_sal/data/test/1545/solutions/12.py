M = 1000000007

n = int(input())
s = input()
a = list(map(int, input().split()))

ans2 = 0
dp = [0] * n + [1]
for i in range(n):
    maxlen = 9001
    for j in range(1, i + 2):
        maxlen = min(maxlen, a[ord(s[i - j + 1]) - ord('a')])
        if maxlen >= j:
            dp[i] = (dp[i] + dp[i - j]) % M
        else:
            break
        ans2 = max(ans2, j)


print(dp[n - 1])
print(ans2)

ans3 = 1
acc = 0
maxlen = 9001
for i in range(n):
    acc += 1
    maxlen = min(maxlen, a[ord(s[i]) - ord('a')])
    if acc > maxlen:
        acc = 1
        ans3 += 1
        maxlen = a[ord(s[i]) - ord('a')]

print(ans3)
