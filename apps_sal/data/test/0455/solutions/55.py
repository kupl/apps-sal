N = int(input())
Q = [list(map(int, input().split())) for i in range(N)]

# 全体の偶奇が一致しているか
tmp = set()
for X, Y in Q:
    tmp.add((X + Y) % 2)
if len(tmp) != 1:
    print((-1))
    return

# 2べきの腕を用意
D = [2 ** i for i in range(30, -1, -1)]

# 偶数なら長さ1の腕を一本追加しておく
if 0 in tmp:
    D.append(1)

# 答えを作る
print((len(D)))
print((" ".join(map(str, D))))

move = [(1, 0, "R"), (-1, 0, "L"), (0, 1, "U"), (0, -1, "D")]
for X, Y in Q:
    nx, ny = 0, 0
    ans = ""
    for d in D:
        tmp_move_ans = ""
        tmp_move = None
        min_move_cost = float('inf')
        for mx, my, s in move:
            cost = abs(nx + mx * d - X) + abs(ny + my * d - Y)
            if cost < min_move_cost:
                tmp_move_ans = s
                min_move_cost = cost
                tmp_move_x = mx
                tmp_move_y = my

        ans += tmp_move_ans
        nx, ny = nx + tmp_move_x * d, ny + tmp_move_y * d
    print(ans)

