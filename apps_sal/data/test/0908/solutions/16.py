import math as m

n = int(input());
cost = list(map(int, input().split()));
s = [];
sr = [];
for i in range(n):
    s.append(list(input()));
    sr.append(list(reversed(s[i])));

dp = [[0, 0] for i in range(n + 1)];
flag = 0;
dp[0][1] = cost[0];
for i in range(1, n):
    if dp[i - 1][0] == -1 and dp[i - 1][1] == -1:
        flag = 1;
        break;

    elif dp[i - 1][0] != -1 and dp[i - 1][1] == -1:
        if s[i] >= s[i - 1]:
            dp[i][0] = dp[i - 1][0];
        else:
            dp[i][0] = -1;
        if sr[i] >= s[i - 1]:
            dp[i][1] = dp[i - 1][0] + cost[i];
        else:
            dp[i][1] = -1;

    elif dp[i - 1][0] == -1 and dp[i - 1][1] != -1:
        if s[i] >= sr[i - 1]:
            dp[i][0] = dp[i - 1][1];
        else:
            dp[i][0] = -1;
        if sr[i] >= sr[i - 1]:
            dp[i][1] = dp[i - 1][1] + cost[i];
        else:
            dp[i][1] = -1;
    else:
        if s[i] >= s[i - 1] and s[i] >= sr[i - 1]:
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]);
        elif s[i] >= s[i - 1] and s[i] < sr[i - 1]:
            dp[i][0] = dp[i - 1][0]
        elif s[i] < s[i - 1] and s[i] >= sr[i - 1]:
            dp[i][0] = dp[i - 1][1];
        else:
            dp[i][0] = -1;

        if sr[i] >= s[i - 1] and sr[i] >= sr[i - 1]:
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i];
        elif sr[i] >= s[i - 1] and sr[i] < sr[i - 1]:
            dp[i][1] = dp[i - 1][0] + cost[i];
        elif sr[i] < s[i - 1] and sr[i] >= sr[i - 1]:
            dp[i][1] = dp[i - 1][1] + cost[i];
        else:
            dp[i][1] = -1;

if flag == 1:
    print((-1));
else:
    res = max(dp[n - 1][0], dp[n - 1][1]) if min(dp[n - 1][0], dp[n - 1][1]) == -1 else min(dp[n - 1][0], dp[n - 1][1]);
    print(res);


