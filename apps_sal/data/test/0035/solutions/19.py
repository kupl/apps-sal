n, m = (int(i) for i in input().split())
flag = []
for i in range(n):
    flag += [input()]


count = {"R": 0, "G": 0, "B": 0}

for line in flag:
    for let in line:
        count[let] += 1
check1 = True
change1 = 0
for i in range(n):
    if i < n - 1 and flag[i][0] != flag[i + 1][0]:
        change1 += 1
    for j in range(m):
        if j < m - 1 and flag[i][j] != flag[i][j + 1]:
            check1 = False
if change1 != 2 or len({count["R"], count["G"], count["B"]}) > 1:
    check1 = False


check2 = True
change2 = 0
for j in range(m):
    if j < m - 1 and flag[0][j] != flag[0][j + 1]:
        change2 += 1
    for i in range(n):
        if i < n - 1 and flag[i][j] != flag[i + 1][j]:
            check2 = False
if change2 != 2 or len({count["R"], count["G"], count["B"]}) > 1:
    check2 = False

if check2 or check1:
    print("YES")
else:
    print("NO")
