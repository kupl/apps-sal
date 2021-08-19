n = int(input().strip())
dp = [0] * (n + 1)
cur_factor = 2
color = 1
while cur_factor <= n:
    if not dp[cur_factor]:
        multiple = cur_factor
        while multiple <= n:
            if not dp[multiple]:
                dp[multiple] = color
            multiple += cur_factor
        color += 1
    cur_factor += 1
print(' '.join(map(str, dp[2:n + 1])))
