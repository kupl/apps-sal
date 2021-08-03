def R(): return map(int, input().split())


f = open('input.txt', 'r')
n, arr = int(f.readline()), list(map(int, f.readline().split()))
dp = [0] * n
for i in range(n):
    dp[i] = dp[i - 1] + (1 if arr[i] >= 0 else 0)
acc = 0
res = n
for i in range(n - 2, -1, -1):
    acc += 1 if arr[i + 1] <= 0 else 0
    res = min(res, acc + dp[i])
print(res, file=open('output.txt', 'w'))
