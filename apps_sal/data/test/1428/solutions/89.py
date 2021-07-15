from itertools import permutations
n,n_color = map(int,input().split())
change_cost = [list(map(int, input().split())) for i in range(n_color)]
color_grid = [list(map(int, input().split())) for i in range(n)]

mod0_colors = [0] * n_color
mod1_colors = [0] * n_color
mod2_colors = [0] * n_color
for y in range(n):
    for x in range(n):
        color = color_grid[y][x]-1
        if (y+x+2) % 3 == 0:
            mod0_colors[color]+= 1
        elif (y+x+2) % 3 == 1:
            mod1_colors[color]+= 1
        else:
            mod2_colors[color]+= 1

mod2color_cost = [[0]*n_color for _ in range(3)]
for mod,mod_colors in enumerate([mod0_colors,mod1_colors,mod2_colors]):
    for color_to in range(n_color):
        total_cost = 0
        for color_from in range(n_color):
            cost_per_node = change_cost[color_from][color_to]
            n_node = mod_colors[color_from]
            total_cost += n_node*cost_per_node
        mod2color_cost[mod][color_to] = total_cost

ans = float('inf')
for pettern in permutations([i for i in range(n_color)],3):
    total_cost = 0
    for from_ in range(3):
        to = pettern[from_]
        total_cost += mod2color_cost[from_][to]
    ans = min(ans, total_cost)
print(ans)
