x = []
for i in range(8):
    x.append(input())
B_mov = 1000
for i in range(8):
    for j in range(8):
        if x[i][j] == "B":
            count = 0
            for k in range(i + 1, 8):
                if x[k][j] == ".":
                    count += 1
                else:
                    break
            else:
                if count < B_mov:
                    B_mov = count
            count = 0
A_mov = 1000
for i in range(8):
    for j in range(8):
        if x[i][j] == "W":
            count = 0
            for k in range(i - 1, -1, -1):
                if x[k][j] == ".":
                    count += 1
                else:
                    break
            else:
                if count < A_mov:
                    A_mov = count
            count = 0
if A_mov > B_mov:
    print("B")
else:
    print("A")
