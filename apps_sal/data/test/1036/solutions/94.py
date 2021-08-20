(n, k) = map(int, input().split())
s = input()
power = [1]
for i in range(k):
    power.append(power[-1] * 2 % n)
dp = list(s)
for j in range(k):
    ndp = [None] * n
    for i in range(n):
        a = dp[i]
        b = dp[(i + power[j]) % n]
        if a == 'R':
            ndp[i] = a if b == 'S' else b
        elif a == 'P':
            ndp[i] = a if b == 'R' else b
        else:
            ndp[i] = a if b == 'P' else b
    dp = ndp
print(dp[0])
