N = int(input())
if N == 1:
    print(1)
    return
mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))
    if 0 in mat[i]:
        zero_pos = (i, mat[i].index(0))

# 和を求めておく
if zero_pos[0] == 0:
    v_sum = sum(mat[1])
else:
    v_sum = sum(mat[0])

# 和から0を埋める
zero_row_sum = sum(mat[zero_pos[0]])
if v_sum - zero_row_sum <= 0:
    print(-1)
    return
mat[zero_pos[0]][zero_pos[1]] = v_sum - zero_row_sum

# row check
for i in range(N):
    row_sum = sum(mat[i])
    if row_sum != v_sum:
        print(-1)
        return

# col check
for j in range(N):
    col_sum = sum([mat[i][j] for i in range(N)])
    if col_sum != v_sum:
        print(-1)
        return

# diag check
diag_sum = sum([mat[i][i] for i in range(N)])
if diag_sum != v_sum:
    print(-1)
    return

# inv diag check
inv_diag_sum = sum([mat[i][N - i - 1] for i in range(N)])
if inv_diag_sum != v_sum:
    print(-1)
    return

print(mat[zero_pos[0]][zero_pos[1]])
