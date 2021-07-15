import sys

input = sys.stdin.readline

roads = []

for i in range(4):
    roads.append([int(x) for x in input().split()])

clock = {}
cclock = {}
opp = {}

clock[0] = 1
clock[1] = 2
clock[2] = 3
clock[3] = 0

cclock[1] = 0
cclock[2] = 1
cclock[3] = 2
cclock[0] = 3

opp[0] = 2
opp[1] = 3
opp[2] = 0
opp[3] = 1

for i in range(4):
    road = roads[i]
    if road[3] == 1:
        if road[0] == 1 or road[1] == 1 or road[2] == 1:
            print("YES")
            break
        left = roads[cclock[i]]
        right = roads[clock[i]]
        straight = roads[opp[i]]
        if left[2] == 1 or right[0] == 1 or straight[1] == 1:
            print("YES")
            break
else:
    print("NO")
