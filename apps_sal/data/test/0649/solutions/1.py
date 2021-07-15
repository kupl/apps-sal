import time

coord = set()
flows = int(input())
start = time.time()
t = list(map(int, input().split()))
directions = {0: (0, 1), 1: (1, 1), 2: (1, 0), 3: (1, -1), 4: (0, -1), 5: (-1, -1), 6: (-1, 0), 7: (-1, 1)}
was = [[[[0 for j in range(300)] for i in range(300)] for x in range(31)] for y in range(8)]# np.zeros([600,600,31,8])


def flight(n, x=0, y=0, direction=0):
    if was[direction][n][x][y]:
        #print(x, y, direction, n, len(was))
        return
    was[direction][n][x][y] = 1
    if n:
        for _ in range(t[flows - n]):
            x += directions[direction][0]
            y += directions[direction][1]
            coord.add((x, y))
        flight(n - 1, x, y, (direction + 1) % 8)
        flight(n - 1, x, y, (direction - 1) % 8)

flight(flows)
# print(coord)
print(len(coord))

