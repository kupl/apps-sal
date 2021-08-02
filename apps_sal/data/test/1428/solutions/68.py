# 色の塗り方は全部で何通りか。O(C^3)で、C^3 = 27000通り。
# 各塗り方に対していちいち計算していると最大25000マスで、これだと間に合わない。
# 3つに別れた各部分を各色に変えるコスト合計を前計算しておけば良い。O(C^3 + N^2 C)。
# 一ひねりした全探索。

n, c = list(map(int, input().split()))
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
            if (ci != cj != ck != ci):
                ans = min(ans, cost[0][ci] + cost[1][cj] + cost[2][ck])

print(ans)
