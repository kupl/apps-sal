n, w = list(map(int, input().split()))
pack_list = [list(map(int, input().split())) for _ in range(n)]

# dp = [[float('inf') for _ in range(10**7+1)] for _ in range(n+1)]
# dp[0] = [0 for _ in range(10**7+1)]

dp_dict = {0: {0: 0}}  # w,v

'''
for i,pack in enumerate(pack_list):
    for value,weight in enumerate(dp[i]):
        dp[i+1][value] = min(dp[i][value],dp[i+1][value])
        dp[i+1][value+pack[1]] = min(dp[i+1][value+pack[1]],dp[i][value]+pack[0])

for i,num in enumerate(dp[-1][::-1]):
    if num <= w:
        print(10**7-i)'''

for i, pack in enumerate(pack_list):
    i += 1
    if i not in dp_dict:
        dp_dict[i] = {}
    for weight, v in list(dp_dict[i - 1].items()):
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

for k, v in list(target.items()):
    if k <= w:
        max_num = max(max_num, v)

print(max_num)
