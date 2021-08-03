n = int(input())
seq = [int(n) for n in input().split()]
dp = [0 for n in range(n + 1)]
for j in range(0, n):
    if(seq[j] > seq[j - 1]):
        dp[j] = (dp[j - 1] + 1)
    else:
        dp[j] = 1
seq.append(0)

m = 0
x = 0
for i in range(n - 1, -1, -1):
    m = max(m, dp[i - 1] + 1, x + 1)
    if(i == 0 or i == n - 1 or seq[i - 1] + 1 < seq[i + 1]):
        m = max(m, dp[i - 1] + x + 1)

    if(seq[i] < seq[i + 1]):
        x += 1
    else:
        x = 1

print(m)
