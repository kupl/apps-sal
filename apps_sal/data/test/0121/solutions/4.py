A = []
for _ in range(4):
    A += [list(input())]
found = False


def check(list_of_sigs):
    return list_of_sigs.count('.') == 1 and list_of_sigs.count('x') == 2


for col_offset in range(2):
    for row_offset in range(2):
        found = found or check([A[row_offset][col_offset], A[row_offset + 1][col_offset + 1], A[row_offset + 2][col_offset + 2]])
        found = found or check([A[row_offset][3 - col_offset], A[row_offset + 1][2 - col_offset], A[row_offset + 2][1 - col_offset]])
for col in range(2):
    for row in range(4):
        found = found or check([A[row][col], A[row][col + 1], A[row][col + 2]])
for col in range(4):
    for row in range(2):
        found = found or check([A[row][col], A[row + 1][col], A[row + 2][col]])
if found:
    print('YES')
else:
    print('NO')
