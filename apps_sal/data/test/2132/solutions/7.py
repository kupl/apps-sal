MAX_SPEED = 300
n = int(input())
actions = [list(map(int, input().split())) for _ in range(n)]
speed = [0 for i in range(n)]
for i in range(n):
    if actions[i][0] == 1:
        lastSpeed = actions[i][1]
    speed[i] = lastSpeed
ignored = 0
overtook = False
maxSpeed = -1
for i in range(n - 1, -1, -1):
    maxSpeed = max(maxSpeed, speed[i])
    if actions[i][0] == 1:
        pass
    elif actions[i][0] == 2:
        overtook = True
    elif actions[i][0] == 3:
        if maxSpeed > actions[i][1]:
            ignored += 1
        else:
            maxSpeed = speed[i - 1]
    elif actions[i][0] == 4:
        overtook = False
    elif actions[i][0] == 5:
        maxSpeed = speed[i - 1]
    elif actions[i][0] == 6:
        if overtook:
            ignored += 1
print(ignored)
