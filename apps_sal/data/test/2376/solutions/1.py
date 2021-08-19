(n, w) = list(map(int, input().split()))
pack_list = [list(map(int, input().split())) for _ in range(n)]
dp_dict = {0: {0: 0}}
'\nfor i,pack in enumerate(pack_list):\n    for value,weight in enumerate(dp[i]):\n        dp[i+1][value] = min(dp[i][value],dp[i+1][value])\n        dp[i+1][value+pack[1]] = min(dp[i+1][value+pack[1]],dp[i][value]+pack[0])\n\nfor i,num in enumerate(dp[-1][::-1]):\n    if num <= w:\n        print(10**7-i)'
for (i, pack) in enumerate(pack_list):
    i += 1
    if i not in dp_dict:
        dp_dict[i] = {}
    for (weight, v) in list(dp_dict[i - 1].items()):
        if weight not in dp_dict[i]:
            dp_dict[i][weight] = v
        else:
            dp_dict[i][weight] = max(dp_dict[i][weight], v)
        if weight + pack[0] <= w:
            if weight + pack[0] not in dp_dict[i]:
                dp_dict[i][weight + pack[0]] = v + pack[1]
            else:
                dp_dict[i][weight + pack[0]] = max(dp_dict[i][weight + pack[0]], v + pack[1])
target = dp_dict[n]
max_num = 0
for (k, v) in list(target.items()):
    if k <= w:
        max_num = max(max_num, v)
print(max_num)
