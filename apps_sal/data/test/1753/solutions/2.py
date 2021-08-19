s = input().split()
n = int(s[0])
m = int(s[1])
col = []
for i in range(n):
    col.append([i])
t = n + 1
for i in range(m):
    s = input().split()
    a = int(s[0]) - 1
    b = int(s[1]) - 1
    col[a].append(t)
    col[b].append(t)
    t += 1
for i in range(len(col)):
    print(len(col[i]))
    for j in range(len(col[i])):
        print(i + 1, col[i][j] + 1)
