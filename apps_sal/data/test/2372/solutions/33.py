def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    h, w = list(map(int, input().split()))
    ch, cw = list(map(int, input().split()))
    dh, dw = list(map(int, input().split()))
    # 迷路の四方を##で囲む。
    # 移動で枠外にでてしまってindexがないことを阻止するための
    # if文を回避
    maze = ['#' * (w + 4)]
    maze.append('#' * (w + 4))
    for _ in range(h):
        maze.append('##' + input()[:-1] + '##')
    maze.append('#' * (w + 4))
    maze.append('#' * (w + 4))
    visited = [[-1] * (w + 4) for _ in range(h + 4)]
    for i in range(h + 4):
        for j in range(w + 4):
            if maze[i][j] == '#':
                visited[i][j] = -2
    # この条件ではindexを+1しないとダメ
    ch += 1
    cw += 1
    dh += 1
    dw += 1
    visited[ch][cw] = 0
    walk = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    telepo = [[i, j] for i in range(-2, 3) for j in range(-2, 3)]

    q_walk = deque([[ch, cw]])
    q_telepo = deque([])
    while q_walk:
        yw, xw = q_walk.popleft()
        # 行った場所を管理
        q_telepo.append([yw, xw])
        for i, j in walk:
            ny, nx = yw + i, xw + j
            # if ny < 0 or h <= ny or nx < 0 or w <= nx:
            #     continue
            if visited[ny][nx] == -1:
                # 行ったことあれば0にしていく
                visited[ny][nx] = visited[yw][xw]
                q_walk.append([ny, nx])
        # 歩ける場所なくなったらワープ
        if len(q_walk) == 0:
            while q_telepo:
                yt, xt = q_telepo.popleft()
                for i, j in telepo:
                    my, mx = yt + i, xt + j
                    # if my < 0 or h <= my or mx < 0 or w <= mx:
                    #     continue
                    # 次がまだ行ったことないところだったら、今までの値に+1
                    # つまり、テレポートしないといけない場所
                    if visited[my][mx] == -1:
                        visited[my][mx] = visited[yt][xt] + 1
                        q_walk.append([my, mx])
    print((visited[dh][dw]))


def __starting_point():
    main()


__starting_point()
