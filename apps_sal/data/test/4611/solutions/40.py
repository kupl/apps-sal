n_num = int(input())
plan_list = [[0, (0, 0)]]


def movable(p1, p2):
    time = p2[0] - p1[0]
    distance = 0

    distance += abs(p1[1][0] - p2[1][0])
    distance += abs(p1[1][1] - p2[1][1])

    if distance > time:
        return 0
    else:
        if (time - distance) % 2 != 0:
            return 0
        else:
            return 1


for _ in range(n_num):
    line = [int(i) for i in input().split()]
    plan_list.append([line[0], (line[1], line[2])])

vector = (0, 0)

flag = 0
for n in range(1, n_num + 1):
    if movable(plan_list[n - 1], plan_list[n]) == 0:
        flag = 1

if flag == 1:
    print('No')
else:
    print('Yes')
