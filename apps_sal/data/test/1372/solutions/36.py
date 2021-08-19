a = list(map(int, input().split()))
HP = a[0]
x = []
for i in range(a[1]):
    (x1, y1) = [int(i) for i in input().split()]
    x.append((x1, y1))
max_tup = max(x, key=lambda x: x[0])
max_a = max_tup[0]
dp = [0] * (HP + max_a)
for i in range(1, len(dp)):
    dp[i] = min((dp[i - a] + b for (a, b) in x))
print(dp[HP])
