(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
num_of_matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = ['x'] * (n + 8)
dp[0] = ''
for i in range(n + 1):
    if dp[i] == 'x':
        continue
    for aa in a:
        x = dp[i + num_of_matches[aa]]
        y = dp[i] + str(aa)
        if x == 'x':
            dp[i + num_of_matches[aa]] = y
        elif len(x) < len(y):
            dp[i + num_of_matches[aa]] = y
        elif len(x) == len(y):
            if x < y:
                dp[i + num_of_matches[aa]] = y
print(dp[n])
