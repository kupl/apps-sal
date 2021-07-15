import sys
from collections import deque

input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    h, w, k = map(int, input().strip().split())
    x1, y1, x2, y2 = map(int, input().strip().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    m = []
    costs1 = [[None for j in range(w)] for i in range(h)]
    costs2 = [[None for j in range(w)] for i in range(h)]
    for _ in range(h):
        m.append(list(input().strip()))
    q1 = deque()
    q1.append((x1, y1, 0))
    costs1[x1][y1] = 0
    q2 = deque()
    q2.append((x2, y2, 0))
    costs2[x2][y2] = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q1 and q2:
        (x, y, cost) = q1.popleft()
        if not costs2[x][y] is None:
            print(cost + costs2[x][y])
            return
        for (add_x, add_y) in directions:
            for dist in range(1, k + 1):
                new_x = x + add_x * dist
                new_y = y + add_y * dist
                if new_x >= h or new_x < 0 or new_y >= w or new_y < 0 or m[new_x][new_y] == '@' or ((not costs1[new_x][new_y] is None) and costs1[new_x][new_y] < cost + 1):
                    break
                if costs1[new_x][new_y] is None:
                    costs1[new_x][new_y] = cost + 1
                    q1.append((new_x, new_y, cost + 1))
        (x, y, cost) = q2.popleft()
        if not costs1[x][y] is None:
            print(cost + costs1[x][y])
            return
        for (add_x, add_y) in directions:
            for dist in range(1, k + 1):
                new_x = x + add_x * dist
                new_y = y + add_y * dist
                if new_x >= h or new_x < 0 or new_y >= w or new_y < 0 or m[new_x][new_y] == '@' or ((not costs2[new_x][new_y] is None) and costs2[new_x][new_y] < cost + 1):
                    break
                if costs2[new_x][new_y] is None:
                    costs2[new_x][new_y] = cost + 1
                    q2.append((new_x, new_y, cost + 1))
    print("-1")


def __starting_point():
    main()

__starting_point()
