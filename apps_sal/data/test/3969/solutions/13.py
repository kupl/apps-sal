# Basta encontrar la medida del mayor subarray que es no-decreciente.
# Con cada inserción podemos aumentar este número en 1.

n = int(input().split()[0])
a = []
for _ in range(n):
    a.append(int(input().split()[0]))
dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] <= a[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
print(n - max(dp))
