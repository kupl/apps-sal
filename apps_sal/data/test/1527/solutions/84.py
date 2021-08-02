from collections import deque
H, W = list(map(int, input().split()))
l = [list(input()) for i in range(H)]
l_count = [[0] * W for i in range(H)]


def answer(st_X, st_Y):  # X,Y座標を指定してそこからの距離を考える
    tmp_X, tmp_Y = st_X, st_Y
    que = deque([[tmp_X, tmp_Y]])
    after = set()
    while que:  # スタート地点からの距離を数えながら行ったことのない場所を探索する
        tmp_X, tmp_Y = que.popleft()
        nu = l_count[tmp_Y][tmp_X]
        after.add((tmp_X, tmp_Y))
        if tmp_X > 0 and l[tmp_Y][tmp_X - 1] == "." and (tmp_X - 1, tmp_Y) not in after and [tmp_X - 1, tmp_Y] not in que:
            l_count[tmp_Y][tmp_X - 1] = nu + 1
            que.append([tmp_X - 1, tmp_Y])
        if tmp_Y > 0 and l[tmp_Y - 1][tmp_X] == "." and (tmp_X, tmp_Y - 1) not in after and [tmp_X, tmp_Y - 1] not in que:
            l_count[tmp_Y - 1][tmp_X] = nu + 1
            que.append([tmp_X, tmp_Y - 1])
        if tmp_X < W - 1 and l[tmp_Y][tmp_X + 1] == "." and (tmp_X + 1, tmp_Y) not in after and [tmp_X + 1, tmp_Y] not in que:
            l_count[tmp_Y][tmp_X + 1] = nu + 1
            que.append([tmp_X + 1, tmp_Y])
        if tmp_Y < H - 1 and l[tmp_Y + 1][tmp_X] == "." and (tmp_X, tmp_Y + 1) not in after and [tmp_X, tmp_Y + 1] not in que:
            l_count[tmp_Y + 1][tmp_X] = nu + 1
            que.append([tmp_X, tmp_Y + 1])


ans = 0
for i in range(H):
    for j in range(W):
        if l[i][j] == ".":
            l_count = [[0] * W for i in range(H)]
            answer(j, i)
            tmp = max(sum(l_count, []))
            ans = max(ans, tmp)
print(ans)
