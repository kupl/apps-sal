
import sys
input = sys.stdin.readline
INF = float('inf')


def inpl(): return list(map(int, input().split()))


def move_uv(x, y):
    ut = x + y
    vt = x - y
    command = ''
    u, v = 0, 0
    for i in range(len(D)):
        if u <= ut and v <= vt:
            command += 'R'
            u += D[i]
            v += D[i]
        elif u <= ut and v > vt:
            command += 'U'
            u += D[i]
            v -= D[i]
        elif u > ut and v <= vt:
            command += 'D'
            u -= D[i]
            v += D[i]
        else:
            command += 'L'
            u -= D[i]
            v -= D[i]

    return command


N = int(input())
point = []
max_length = 0
for i in range(N):
    x, y = inpl()
    max_length = max(max_length, abs(x) + abs(y))
    point.append([x, y])

parity = sum(point[0]) % 2
judge = True
for p in point:
    if parity ^ sum(p) % 2:
        judge = False
        break

if not judge:
    print((-1))
else:
    D = [2 ** i for i in range(len(bin(max_length)) - 1)]
    D.reverse()

    if parity == 0:
        D.append(1)
    print((len(D)))
    print((' '.join(map(str, D))))
    for i in range(N):
        print((move_uv(point[i][0], point[i][1])))
