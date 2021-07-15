have = list(map(int, input().split()))
goal = list(map(int, input().split()))
deficit = 0
makeable = 0
for i in range(3):
    if have[i] < goal[i]:
        deficit += goal[i] - have[i]
    else:
        makeable += (have[i] - goal[i]) // 2
print('Yes' if makeable >= deficit else 'No')

