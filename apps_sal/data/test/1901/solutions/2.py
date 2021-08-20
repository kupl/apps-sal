from collections import deque
start = list(map(int, input().strip().split()))
cost = list(map(int, input().strip().split()))
dp = dict()
for _ in range(start[1]):
    k = list(map(int, input().strip().split()))
    if k[0] - 1 not in dp:
        dp[k[0] - 1] = dict()
    if k[1] - 1 not in dp:
        dp[k[1] - 1] = dict()
    dp[k[0] - 1][k[1] - 1] = 0
    dp[k[1] - 1][k[0] - 1] = 0
counted = dict()
answer = 0
for (index, value) in enumerate(cost):
    if index not in dp:
        answer += value
    elif index in counted:
        continue
    else:
        now = index
        plus = value
        counted[index] = 0
        dec = deque()
        for key in dp[now]:
            dec.append(key)
        while len(dec) > 0:
            k = dec.popleft()
            if k in counted:
                continue
            plus = min(plus, cost[k])
            counted[k] = 0
            if k in dp:
                for key in dp[k]:
                    dec.append(key)
        answer += plus
print(answer)
