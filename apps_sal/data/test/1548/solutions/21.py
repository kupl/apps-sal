Scount = int(input())
sticks = [int(x) for x in input().split(' ')]
sticks.sort()
horizontal = 0
for i in range(Scount - 1, Scount // 2 - 1, -1):
    horizontal += sticks[i]
vertical = 0
for i in range(Scount // 2 - 1, -1, -1):
    vertical += sticks[i]
print(horizontal ** 2 + vertical ** 2)
