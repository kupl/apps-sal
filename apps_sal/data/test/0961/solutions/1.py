n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
f, l = {}, {}
for i in range(len(a)):
    x = a[i]
    if x not in f:
        f[x] = i
    l[x] = i
pr = [a[0]]

for i in range(1, len(a) + 1):
    j = i
    mx = 0
    nums = set()
    curxor = 0
    b = i
    while j > 0:
        x = a[j - 1]
        if l[x] > i - 1:
            break
        if x not in nums:
            nums.add(x)
            curxor ^= x
        b = min(b, f[x] + 1)
        if b == j:
            mx = max(mx, dp[j - 1] + curxor)
        j -= 1
    dp[i] = max(dp[i - 1], mx)
print(dp[len(a)])
