n,m = list(map(int, input().split()))
x_count = 0
start_x = 0
start_y = 0
p = []
for i in range(n):
    p.append(input())
started = False
for i in range(n):
    for j in range(m):
        if p[i][j] == 'X':
            x_count += 1
        if p[i][j] == 'X' and not started:
            started = True
            start_x = i
            start_y = j
x_len = 0
for i in range(start_x, n):
    if p[i][start_y] == "X":
        x_len += 1
    else:
        break
y_len = 0
for i in range(start_y, m):
    if p[start_x][i] == "X":
        y_len += 1
    else:
        break
if x_len * y_len != x_count:
    print("NO")
    return
for i in range(start_x, start_x + x_len):
    for j in range(start_y, start_y + y_len):
        if p[i][j] != 'X':
            print("NO")
            return
print("YES")

