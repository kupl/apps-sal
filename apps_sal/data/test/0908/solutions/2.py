n = int(input())
e = list(map(int, input().split()))
dp = [[0, 0], [0, 0]]
s_prev = input().strip()
dp[0][1] = e[0]
ans = -1
for i in range(n - 1):
    cur_pos = (i + 1) % 2
    prev_pos = i % 2
    s_cur = input().strip()
    (a, b) = (0, 0)
    if dp[prev_pos][0] != -1 and s_prev <= s_cur:
        a = dp[prev_pos][0]
    else:
        a = -1
    if dp[prev_pos][1] != -1 and s_prev[::-1] <= s_cur:
        b = dp[prev_pos][1]
    else:
        b = -1
    if a == -1 and b == -1:
        dp[cur_pos][0] = -1
    elif a == -1:
        dp[cur_pos][0] = b
    elif b == -1:
        dp[cur_pos][0] = a
    else:
        dp[cur_pos][0] = min(a, b)
    if dp[prev_pos][0] != -1 and s_prev <= s_cur[::-1]:
        a = dp[prev_pos][0] + e[i + 1]
    else:
        a = -1
    if dp[prev_pos][1] != -1 and s_prev[::-1] <= s_cur[::-1]:
        b = dp[prev_pos][1] + e[i + 1]
    else:
        b = -1
    if a == -1 and b == -1:
        dp[cur_pos][1] = -1
    elif a == -1:
        dp[cur_pos][1] = b
    elif b == -1:
        dp[cur_pos][1] = a
    else:
        dp[cur_pos][1] = min(a, b)
    s_prev = s_cur
a = dp[(n + 1) % 2][0]
b = dp[(n + 1) % 2][1]
if a == -1 and b == -1:
    print(-1)
elif a == -1:
    print(b)
elif b == -1:
    print(a)
else:
    print(min(a, b))
