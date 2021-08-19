from collections import deque
dp = {}
for i in range(int(input())):
    (x, y) = list(map(int, input().split()))
    if y - x in dp:
        dp[y - x].append((x, y))
    else:
        dp[y - x] = [(x, y)]
for i in dp:
    dp[i].sort()
    dp[i] = deque(dp[i])
w = list(map(int, input().split()))
ans = [0] * len(w)
flag = 1
for i in range(len(w)):
    if not w[i] in dp or not len(dp[w[i]]):
        flag = 0
        break
    ans[i] = dp[w[i]].popleft()
if not flag:
    print('NO')
else:
    for i in range(1, len(ans)):
        if ans[i][0] <= ans[i - 1][0] and ans[i][1] <= ans[i - 1][1]:
            flag = 0
    if not flag:
        print('NO')
    else:
        print('YES')
        for i in ans:
            print(i[0], i[1])
