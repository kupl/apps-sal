import sys
line_count = 0
for line in sys.stdin.readlines():
    inputs = line.split()
    if line_count == 0:
        n = int(inputs[0])
        c = int(inputs[1])
    elif line_count == 1:
        a = []
        for i in range(n - 1):
            a.append(int(inputs[i]))
    elif line_count == 2:
        b = []
        for i in range(n - 1):
            b.append(int(inputs[i]))
    if line_count == 2:
        break
    line_count += 1
by_stair = [0]
by_elev = [c]
print(0, end=' ')
for i in range(1, n):
    pos_stair = min(by_stair[i - 1] + a[i - 1], by_elev[i - 1] + a[i - 1])
    by_stair.append(pos_stair)
    pos_elev = min(by_stair[i - 1] + c + b[i - 1], by_elev[i - 1] + b[i - 1])
    by_elev.append(pos_elev)
    print(min(pos_stair, pos_elev), end=' ')
