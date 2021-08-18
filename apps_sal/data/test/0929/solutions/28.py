H, W = list(map(int, input().split()))
grid = []
for _ in range(H):
    line = list(map(int, input().split()))
    grid.append(line)
q = []
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            q.append([i, j])
    else:
        for j in range(W - 1, -1, -1):
            q.append([i, j])
cnt = 0
op_list = []
for i in range(len(q) - 1):
    if grid[q[i][0]][q[i][1]] % 2 == 0:
        pass
    else:
        grid[q[i][0]][q[i][1]] -= 1
        grid[q[i + 1][0]][q[i + 1][1]] += 1
        cnt += 1
        op_list.append([q[i][0], q[i][1], q[i + 1][0], q[i + 1][1]])
print(cnt)
for op in op_list:
    print((op[0] + 1, op[1] + 1, op[2] + 1, op[3] + 1))
