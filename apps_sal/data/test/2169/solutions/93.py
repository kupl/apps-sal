from collections import defaultdict
H, W, D = list(map(int, input().split()))
grid = [[0] * W for _ in range(H)]
for h in range(H):
    grid[h] = list(map(int, input().split()))
number_yx = [[0, 0] for _ in range(H * W + 1)]
for y in range(H):
    for x in range(W):
        number_yx[grid[y][x]] = [y, x]
fromto_cost = defaultdict(lambda: defaultdict(int))
for mod_group in range(D):
    start = mod_group + 1
    previous = start
    fromto_cost[start][start] = 0
    previous_y, previous_x = number_yx[previous]
    cost = 0
    while previous + D <= (H * W):
        Next = previous + D
        Next_y, Next_x = number_yx[Next]
        cost += abs(Next_y - previous_y) + abs(Next_x - previous_x)
        fromto_cost[start][Next] = cost

        previous = Next
        previous_y, previous_x = Next_y, Next_x

Q = int(input())
ans_ls = [0] * Q
for i in range(Q):
    start, goal = list(map(int, input().split()))
    mod = start % D
    base = mod
    if base == 0:
        base = D
    base_to_goal = fromto_cost[base][goal]
    base_to_start = fromto_cost[base][start]
    ans_ls[i] = base_to_goal - base_to_start
for ans in ans_ls:
    print(ans)
