import sys
line = str.split(input(), ' ')
n = int(line[0])
k = int(line[1])
line = str.split(str(input()), ' ')
speeds = []
for s in line:
    speeds.append(int(s))
sspeeds = speeds
sspeeds.sort()
sspeeds.reverse()
sys.stdout.write(str(sspeeds[k - 1]))
