from collections import deque

nums = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011]
n, k = list(map(int, input().split()))
innums = []
for i in range(n):
    innums.append(int(input(), 2))

sdp = [[30000]*10 for i in range(1<<7)]

for i in range(1<<7):
    for j in range(10):
        # possible to append
        if (i & nums[j]) == i:
            raw = nums[j] - i
            count = 0
            while raw:
                count += 1
                raw -= raw & (-raw)
            sdp[i][j] = count

dp = [[False] * (k + 1) for i in range(n + 1)]

dp[n][0] = True
for idx, num in reversed(list(enumerate(innums))):
    for cost in sdp[num]:
        for k_ in range(cost, k + 1):
            dp[idx][k_] |= dp[idx+1][k_- cost]
if not dp[0][k]:
    print(-1)
else:
    cur_k = k
    ans = []
    for idx, num in enumerate(innums):
        for i, cost in reversed(list(enumerate(sdp[num]))):
            if cost > cur_k:
                continue

            if dp[idx+1][cur_k - cost]:
                cur_k -= cost
                ans.append(i)
                break
    print(''.join(map(str, ans)))

