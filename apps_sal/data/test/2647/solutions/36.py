from collections import deque
import sys
read = sys.stdin.read


def main():
    h, w = map(int, input().split())
    wall_cnt = 0
    gg = list()
    gg.append([1] * (w + 2))
    for _ in range(h):
        row = tuple(input())
        wall_cnt += row.count('
        gg.append([1] + [c == '
    gg.append([1] * (w + 2))

    g2=[[0] * (w + 2) for _ in range(h + 2)]
    g2[1][1]=1
    vs=deque()
    vs.append((1, 1))
    move_y=(0, 1, 0, -1)
    move_x=(1, 0, -1, 0)
    while vs:
        y, x=vs.popleft()
        ys=[y + i for i in move_y]
        xs=[x + i for i in move_x]
        for yse, xse in zip(ys, xs):
            if not gg[yse][xse]:
                vs.append((yse, xse))
                gg[yse][xse]=1
                g2[yse][xse]=g2[y][x] + 1
    if g2[h][w] == 0:
        print(-1)
    else:
        ans=(h * w) - g2[h][w] - wall_cnt
        print(ans)


def __starting_point():
    main()


__starting_point()
