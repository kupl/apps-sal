n = int(input())

no_overtake = 0
speedlimit = [float("inf")]

speed = 0

vio = 0

ot_ignored = False

for _ in range(n):
    cmd = input().split()
    if cmd[0] == '1':
        speed = int(cmd[1])
        while speed > speedlimit[-1]:
            vio += 1
            speedlimit.pop(-1)
    elif cmd[0] == '2':
        if no_overtake and not ot_ignored:
            vio += no_overtake
            ot_ignored = True
    elif cmd[0] == '3':
        speedlimit.append(int(cmd[1]))
        if speed > speedlimit[-1]:
            vio += 1
            speedlimit.pop(-1)
    elif cmd[0] == '4':
        no_overtake = 0
        ot_ignored = False
    elif cmd[0] == '5':
        speedlimit = [float('inf')]
    elif cmd[0] == '6':
        if ot_ignored == 1:
            no_overtake = 0
        no_overtake += 1
        ot_ignored = False

print(vio)

