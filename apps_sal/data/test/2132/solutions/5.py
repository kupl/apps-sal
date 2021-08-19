from collections import deque
n = int(input())
speed_stack = deque()
over_take = 0
speed = 0
penalty = 0


def speed_check(penalty, x):
    while speed_stack and speed_stack[-1] < x:
        speed_stack.pop()
        penalty += 1
    return penalty


for i in range(n):
    update = [int(j) for j in input().split()]
    if update[0] == 1:
        speed = update[1]
        penalty = speed_check(penalty, speed)
    elif update[0] == 2:
        penalty += over_take
        over_take = 0
    elif update[0] == 3:
        speed_stack.append(update[1])
        penalty = speed_check(penalty, speed)
    elif update[0] == 4:
        over_take = 0
    elif update[0] == 5:
        speed_stack = deque()
    else:
        over_take += 1
print(penalty)
