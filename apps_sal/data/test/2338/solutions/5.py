import sys

def dist(p):
    return abs(p[0]) + abs(p[1])

n = int(input())

pts = []
for i in range(n):
    pts.append(tuple(map(int, input().split())))

pts.sort(key=dist)

ops = []

def move(s, t, direc):
    if s == t: return
    if t > s: ops.append('1 {} {}'.format(t - s, direc[0]))
    else: ops.append('1 {} {}'.format(s - t, direc[1]))

for p in pts:
    move(0, p[0], 'RL')
    move(0, p[1], 'UD')
    ops.append('2')
    move(p[0], 0, 'RL')
    move(p[1], 0, 'UD')
    ops.append('3')

sys.stdout.write(str(len(ops))+'\n')
sys.stdout.write('\n'.join(ops))
    




