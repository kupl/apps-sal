import sys

rows = [input() for i in range(4)]
cols = []

for j in range(4):
    col = [rows[i][j] for i in range(4)]
    cols.append("".join(col))

diags = []
diags.append("".join([rows[i][i] for i in range(4)]))
diags.append("".join([rows[0][1], rows[1][2], rows[2][3]]))
diags.append("".join([rows[1][0], rows[2][1], rows[3][2]]))
diags.append("".join([rows[i][3-i] for i in range(4)]))
diags.append("".join([rows[0][2], rows[1][1], rows[2][0]]))
diags.append("".join([rows[1][3], rows[2][2], rows[3][1]]))

strs = rows + cols + diags

winstrs = ["xx.", "x.x", ".xx"]

for winstr in winstrs:
    for s in strs:
        if winstr in s:
            print("YES")
            return
print("NO")

