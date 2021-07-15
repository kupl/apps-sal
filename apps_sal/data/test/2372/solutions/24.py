from collections import deque

def main():
    h, w = list(map(int, input().split()))
    c = list([int(x)+1 for x in input().split()])
    d = list([int(x)+1 for x in input().split()])
    s = ['#'*(w+4)]*2 + ['#'*2 + input() + '#'*2 for _ in range(h)] + ['#'*(w+4)]*2

    ans = [[-1]*(w+4) for _ in range(h+4)]
    for i in range(h+4):
        for j in range(w+4):
            if s[i][j] == '#':
                ans[i][j] = -2
    ans[c[0]][c[1]] = 0

    move1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    move2 = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if abs(i)+abs(j) > 1]

    yet = deque([(c[0], c[1])])
    done = deque()

    while yet:
        y, x = yet.popleft()
        done.append((y, x))
        for dy, dx in move1:
            ydy, xdx = y+dy, x+dx
            if ans[ydy][xdx] == -1:
                yet.append((ydy, xdx))
                ans[ydy][xdx] = ans[y][x]

        if len(yet) == 0:
            while done:
                y, x = done.popleft()
                for dy, dx in move2:
                    ydy, xdx = y+dy, x+dx
                    if ans[ydy][xdx] == -1:
                        ans[ydy][xdx] = ans[y][x] + 1
                        yet.append((ydy, xdx))

    print((ans[d[0]][d[1]]))

def __starting_point():
    main()

__starting_point()
