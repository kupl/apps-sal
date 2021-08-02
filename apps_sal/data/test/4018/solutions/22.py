#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : H.py
# Author            : JCHRYS <jchrys@me.com>
# Date              : 30.08.2019
# Last Modified Date: 30.08.2019
# Last Modified By  : JCHRYS <jchrys@me.com>
class const:
    size = 26;  # size of lowercase alphabet


n, k = list(map(int, input().split()));
s = input();

maxpos = [[-1 for _ in range(const.size)] for _ in range(n)];

for i in range(n):
    for j in range(const.size):
        if i > 0:
            maxpos[i][j] = maxpos[i - 1][j]
    maxpos[i][ord(s[i]) - ord('a')] = i

#print(*[row for row in maxpos], sep="\n")
dp = [[0 for _ in range(n + 1)] for _ in range(n)];

for i in range(n):
    dp[i][1] = 1

for length in range(2, n):
    for endswith in range(1, n):
        for before in range(const.size):
            if maxpos[endswith - 1][before] != -1:
                dp[endswith][length] = dp[endswith][length] + dp[maxpos[endswith - 1][before]][length - 1];


#print(*[row for row in dp], sep="\n")
k -= 1;
ans = 0;
for length in range(n - 1, 0, -1):
    temp = 0;
    for i in range(const.size):
        if (maxpos[n - 1][i] != -1):
            temp += dp[maxpos[n - 1][i]][length];

    if temp >= k:
        ans += k * (n - length);
        k = 0;
        break;
    else:
        k -= temp;
        ans += temp * (n - length);


if (k == 1):
    ans += n;
    k -= 1

if k > 0:
    print(-1)
    return
print(ans)
