(n, c) = list(map(int, input().split()))
change_cost = [list(map(int, input().split())) for _ in range(c)]
init_color = [list(map(int, input().split())) for _ in range(n)]
cost = [[0 for _ in range(c)] for _ in range(3)]
for row in range(n):
    for col in range(n):
        before = init_color[row][col] - 1
        for after in range(c):
            idx = (row + col) % 3
            cost[idx][after] += change_cost[before][after]
ans = 1000 * 500 * 500 * 10
for ci in range(c):
    for cj in range(c):
        for ck in range(c):
            if ci != cj != ck != ci:
                ans = min(ans, cost[0][ci] + cost[1][cj] + cost[2][ck])
print(ans)
